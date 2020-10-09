# -*- coding: utf-8 -*-

"""1. Bài tập về xử lý các trường hợp dữ liệu bị thiếu

Trong bài tập này, chúng ta sẽ làm việc với bộ dữ liệu Housing Prices. 

Tập dữ liệu này có 79 giá trị mô tả (gần như) mọi khía cạnh của các căn nhà ở tại Ames, Iowa.
Với tập dữ liệu này, chúng ta cần xây dựng mô hình để dự đoán giá của mỗi ngôi nhà.

"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Đọc dữ liệu
X_full = pd.read_csv('https://raw.githubusercontent.com/ltdaovn/dataset/master/housing-prices/train.csv',
                     index_col='Id')
X_test_full = pd.read_csv('https://raw.githubusercontent.com/ltdaovn/dataset/master/housing-prices/test.csv',
                          index_col='Id')

# Loại bỏ các căn nhà không có giá
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# Để đơn giản bài toán, ở đây chúng ta chỉ chọn các thuộc tính số
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Chia tập dữ liệu thành 2 tập dữ liệu con là training set và validation set
X_train, X_valid, y_train, y_valid = train_test_split(X, y,
                                                      train_size=0.8,
                                                      test_size=0.2,
                                                      random_state=0)

# Xem các căn nhà đầu tiên trong tập dữ liệu huấn luyện. Chú ý các giá trị bị thiếu.
X_train.head()

"""
# Bước 1: Làm quen với dữ liệu
"""

# Xem mô tả tập dữ liệu huấn luyện
print(X_train.shape)

# Số lượng dữ liệu bị thiếu trong các cột
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

print("Number of houses:", len(X_train))
print("Number of col with missing value:", X_train.isnull().sum()[X_train.isnull().sum() > 0])
# Hãy trả lời các câu hỏi sau đây?

# Có bao nhiêu căn nhà trong tập dữ liệu huấn luyện?
# num_rows = 1168

# Có bao nhiêu cột dữ liệu bị thiếu?
# num_cols_with_missing = 6

nanEntry = X_train.isnull().sum(axis=1)
print("Number of NaN entries:", len(nanEntry[nanEntry > 0]))


# How many missing entries are contained in all of the training data?
# tot_missing = 270

# Theo bạn, phương pháp nào thích hợp nhất để xử lý trường hợp bị thiếu dữ liệu này?
# Phương pháp thích hợp để xử lý các trường hợp này là thay thế các dữ liệu bằng những giá trị trung binh

"""Bước 2: định nghĩa hàm để đo chất lượng của từng phương pháp

Để so sánh chất lượng của các phương pháp, chúng ta cần định nghĩa hàm score_dataset() . 
Hàm được sử dụng trong ví dụ này là hàm Trung bình của sai biệt tuyệt đối (the mean absolute error (MAE)) 
dành cho mô hình rừng ngẫu nhiên (RandomForest).
(https://en.wikipedia.org/wiki/Mean_absolute_error) 
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

def judge(X_train, X_valid, Y_train, Y_valid):
    train_set = pd.concat([X_train, Y_train], axis=1, sort=False)
    valid_set = pd.concat([X_valid, Y_valid], axis=1, sort=False)

    fullset = pd.concat([train_set, valid_set], axis=0, sort=False)
    # PP1: Xoá các hàng dữ liệu bị thiếu
    nonNaNRows = fullset.isnull().sum(axis=1) == 0
    nonNaNset = fullset[nonNaNRows]
    X = nonNaNset.iloc[:, :-1]
    y = nonNaNset.iloc[:, -1]
    # print(len(X))
    X_train, X_valid, y_train, y_valid = train_test_split(X, y,
                                                      train_size=0.8,
                                                      test_size=0.2,
                                                      random_state=0)
    # print('Null in valid set:', X_valid.isnull().sum())
    print('Score dataset with remove: ', score_dataset(X_train, X_valid, y_train, y_valid))
    # PP2: Thay thế tự động bằng giá trị trung bình 
    NaNFileedSet = fullset.fillna(fullset.mean())

    
    X = NaNFileedSet.iloc[:, :-1]
    y = NaNFileedSet.iloc[:, -1]
    # print(len(X))
    X_train, X_valid, y_train, y_valid = train_test_split(X, y,
                                                      train_size=0.8,
                                                      test_size=0.2,
                                                      random_state=0)
    # print('Null in valid set:', X_valid.isnull().sum())
    print('Score dataset with replace na:', score_dataset(X_train, X_valid, y_train, y_valid))

    pass 
judge(X_train, X_valid, y_train, y_valid)
# print()
"""
# Bước 3: 

Trong các phương pháp xử lý dữ liệu bị thiếu bạn đã học,
phương pháp nào cho kết quả dự báo chính xác nhất.
Hãy cho biết giá trị MAE của từng mô hình.

"""
# Score dataset with remove na:  19459.578977777775
# Score dataset with replace na with mean: 16647.91082191781