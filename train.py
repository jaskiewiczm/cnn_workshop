import keras.callbacks as keras_callbacks

from model import model_1


EPOCHS = 64
MODELS_FOLDER = 'models'
BATCH_SIZE = 32


def train():

    epochs = 50
    basic_model = model_1()

    callbacks = [keras_callbacks.EarlyStopping(monitor='val_loss',
                                               patience=8,
                                               verbose=1,
                                               min_delta=1e-4),
                 keras_callbacks.ReduceLROnPlateau(monitor='val_loss',
                                                   factor=0.1,
                                                   patience=4,
                                                   verbose=1,
                                                   epsilon=1e-4),
                 keras_callbacks.ModelCheckpoint(monitor='val_loss',
                                                 filepath=os.path.join(MODELS_FOLDER,
                                                                       'weights-{epoch:04d}-{val_dice_coeff:.2f}.hdf5'),
                                                 save_best_only=True,
                                                 save_weights_only=True)]

    model.fit_generator(
        train_generator(files_train_split, image_directory, mask_directory),
        steps_per_epoch=np.ceil(float(num_train_images) / float(BATCH_SIZE)),
        epochs=EPOCHS,
        verbose=1,
        callbacks=callbacks,
        validation_data=valid_generator(files_valid_split, image_directory, mask_directory),
        validation_steps=np.ceil(float(num_valid_images) / float(BATCH_SIZE)))


train()
