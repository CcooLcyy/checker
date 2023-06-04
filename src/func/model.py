import numpy as np
import cv2 as cv
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder

class MeModel():
    def __init__(self):
        # 加载预训练模型
        # base_model = ResNet50(weights='imagenet', include_top=False)

        # # 添加新的全连接层
        # x = base_model.output
        # x = GlobalAveragePooling2D()(x)
        # x = Dense(4, activation='softmax')(x)
        # self.model = Model(inputs=base_model.input, outputs=x)
        # self.model.save('res/model/pre_train.h5')
        # # 编译模型
        self.model = load_model('res/model/pre_train.h5')
        self.model.compile(optimizer=Adam(learning_rate=0.000001), loss='categorical_crossentropy', metrics=['accuracy'])

    def fit(self, image, label):
        history = self.model.fit(image, label, epochs=20, batch_size=8, validation_split=0.1)
        return history

    def predict(self, image):
        self.label = self.model.predict(image)
        return self.label

    def evaluate(self, image, label):
        loss, acc = self.model.evaluate(image, label)
        acc = acc *100
        print(f'准确率：{acc:.2f}%')

if __name__ == '__main__':
    model = MeModel()