import pandas as pd
import os

class CSVDatabase:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def add_object(self, obj):
        cls_name = obj.__class__.__name__
        file_path = os.path.join(self.data_dir, f'{cls_name}.csv')
        df = pd.DataFrame([obj.__dict__])
        header = not os.path.exists(file_path)
        df.to_csv(file_path, mode='a', header=header, index=False)

    def get_object(self, cls, obj_id):
        cls_name = cls.__name__
        file_path = os.path.join(self.data_dir, f'{cls_name}.csv')
        df = pd.read_csv(file_path)
        obj_data = df[df['id'] == obj_id].iloc[0].to_dict()
        return cls(**obj_data)

    def update_object(self, obj):
        cls_name = obj.__class__.__name__
        file_path = os.path.join(self.data_dir, f'{cls_name}.csv')
        df = pd.read_csv(file_path)
        df.loc[df['id'] == obj.id] = obj.__dict__
        df.to_csv(file_path, index=False)

    def delete_object(self, cls, obj_id):
        cls_name = cls.__name__
        file_path = os.path.join(self.data_dir, f'{cls_name}.csv')
        df = pd.read_csv(file_path)
        df = df[df['id'] != obj_id]
        df.to_csv(file_path, index=False)
