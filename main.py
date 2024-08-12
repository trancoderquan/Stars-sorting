
import machine as mc


dr='Stars.csv'
train_feature, test_feature, train_label, test_label, unique_label, unique_cat, unique_color,mean,scale = mc.data_process(dr)

model = mc.build_model()
trained_epochs, accuracy, loss, val_acc, val_loss = mc.train_model(model, train_feature, train_label, test_feature, test_label)
mc.plot_loss_curve(trained_epochs,  accuracy, loss, val_acc, val_loss)


model.save('star classification')
