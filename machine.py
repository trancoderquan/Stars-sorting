import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def input_process(unique_cat, unique_color,mean,scale, input):

    input[4] = np.char.lower(input[4])
    input[4] = np.char.replace(input[4], ' ', '')
    input[4] = np.char.replace(input[4], '-', '')

    input[5] = np.char.lower(input[5])
    input[5] = np.char.replace(input[5], ' ', '')
    input[5] = np.char.replace(input[5], '-', '')
    clr = input[4]
    clss = input[5]
    input[4] = unique_cat.tolist().index(clr)
    input[5] = unique_color.tolist().index(clss)
    for i in range(len(input)):
        input[i] = (float(input[i]) - mean[i]) / scale[i]
        input[i] = float(input[i])

    input = np.reshape(input, (1, -1))
    return input

def data_process(dr):
    #load
    feature = pd.read_csv(dr,
                          usecols=['Temperature (K)', 'Luminosity (L/Lo)', 'Radius (R/Ro)', 'Absolute magnitude (Mv)',
                                   'Star category', 'Star color'])
    feature = feature.to_numpy()
    for i in range(len(feature[:,4])):
        feature[i, 4] = np.char.lower(feature[i, 4])
        feature[i, 4] = np.char.replace(feature[i, 4], ' ', '')
        feature[i, 4] = np.char.replace(feature[i, 4], '-', '')
    for i in range(len(feature[:, 5])):
        feature[i, 5] = np.char.lower(feature[i, 5])
        feature[i, 5] = np.char.replace(feature[i, 5], ' ', '')
        feature[i, 5] = np.char.replace(feature[i, 5], '-', '')
    label = pd.read_csv(dr, usecols=['Spectral Class'])
    label = label.to_numpy()

    #process
    unique_cat =np.unique(feature[:, 4], return_inverse=True)[0]
    unique_color = np.unique(feature[:, 5], return_inverse=True)[0]

    feature[:, 4] = np.unique(feature[:, 4], return_inverse=True)[1].tolist()
    feature[:, 5] = np.unique(feature[:, 5], return_inverse=True)[1].tolist()

    unique_label = np.unique(label, return_inverse=True)[0]
    label = (np.unique(label, return_inverse=True)[1]).tolist()

    scaler = StandardScaler()
    feature = scaler.fit_transform(feature)
    label = np.asarray(label).astype('float32')
    mean = scaler.mean_
    scale = scaler.scale_

    train_feature, test_feature, train_label, test_label = train_test_split(feature, label, test_size=0.2, random_state=42)

    return train_feature, test_feature, train_label, test_label, unique_label, unique_cat, unique_color,mean,scale

def build_model ():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(6,)),
        tf.keras.layers.Dense(6, activation='relu'),
        tf.keras.layers.Dense(6, activation='relu'),
        tf.keras.layers.Dense(7, activation='softmax')
                  ])
    model.compile(optimizer=tf.keras.optimizers.Adamax(learning_rate= 0.01),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    return model

def train_model (model, feature, label, test_feature, test_label):
    history = model.fit(feature, label, epochs=125, batch_size=6, validation_data=(test_feature, test_label))
    trained_epochs = history.epoch
    history_df = pd.DataFrame(history.history)
    accuracy = history_df['accuracy']
    loss = history_df['loss']
    val_acc = history_df['val_accuracy']
    val_loss = history_df['val_loss']
    return trained_epochs, accuracy, loss, val_acc, val_loss

def plot_loss_curve(epochs,  accuracy, loss, val_acc, val_loss):
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.plot(epochs, accuracy)
    plt.plot(epochs, val_acc)
    plt.show()
    plt.plot(epochs, loss)
    plt.plot(epochs, val_loss)
    plt.show()