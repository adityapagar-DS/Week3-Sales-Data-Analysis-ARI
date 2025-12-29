{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4915325d-170f-4e44-8326-517f0a6e484f",
   "metadata": {},
   "source": [
    "# Analyze Sales - Calculate revenue, find best product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "838c5aac-fca5-44fd-a99e-7ecd3af18015",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ced58807-4e21-4f35-b33b-171100a02232",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"C:/Users/Hp/Downloads/sales_data (1).csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aded101d-2e21-43bd-82ff-104ce4092826",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Price</th>\n",
       "      <th>Customer_ID</th>\n",
       "      <th>Region</th>\n",
       "      <th>Total_Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>Phone</td>\n",
       "      <td>7</td>\n",
       "      <td>37300</td>\n",
       "      <td>CUST001</td>\n",
       "      <td>East</td>\n",
       "      <td>261100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2024-01-02</td>\n",
       "      <td>Headphones</td>\n",
       "      <td>4</td>\n",
       "      <td>15406</td>\n",
       "      <td>CUST002</td>\n",
       "      <td>North</td>\n",
       "      <td>61624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2024-01-03</td>\n",
       "      <td>Phone</td>\n",
       "      <td>2</td>\n",
       "      <td>21746</td>\n",
       "      <td>CUST003</td>\n",
       "      <td>West</td>\n",
       "      <td>43492</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2024-01-04</td>\n",
       "      <td>Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>30895</td>\n",
       "      <td>CUST004</td>\n",
       "      <td>East</td>\n",
       "      <td>30895</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2024-01-05</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>8</td>\n",
       "      <td>39835</td>\n",
       "      <td>CUST005</td>\n",
       "      <td>North</td>\n",
       "      <td>318680</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date     Product  Quantity  Price Customer_ID Region  Total_Sales\n",
       "0  2024-01-01       Phone         7  37300     CUST001   East       261100\n",
       "1  2024-01-02  Headphones         4  15406     CUST002  North        61624\n",
       "2  2024-01-03       Phone         2  21746     CUST003   West        43492\n",
       "3  2024-01-04  Headphones         1  30895     CUST004   East        30895\n",
       "4  2024-01-05      Laptop         8  39835     CUST005  North       318680"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "40670900-13c9-448e-96e4-f3466b813ac7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100, 7)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1e1fec26-161a-41fe-9cd9-9e04f0313116",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 100 entries, 0 to 99\n",
      "Data columns (total 7 columns):\n",
      " #   Column       Non-Null Count  Dtype \n",
      "---  ------       --------------  ----- \n",
      " 0   Date         100 non-null    object\n",
      " 1   Product      100 non-null    object\n",
      " 2   Quantity     100 non-null    int64 \n",
      " 3   Price        100 non-null    int64 \n",
      " 4   Customer_ID  100 non-null    object\n",
      " 5   Region       100 non-null    object\n",
      " 6   Total_Sales  100 non-null    int64 \n",
      "dtypes: int64(3), object(4)\n",
      "memory usage: 5.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1b96cc8f-fb46-4136-aed6-c04e10c99714",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Date', 'Product', 'Quantity', 'Price', 'Customer_ID', 'Region',\n",
       "       'Total_Sales'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "851e5d38-8cf3-44a4-9756-9480dff61fe4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Price</th>\n",
       "      <th>Customer_ID</th>\n",
       "      <th>Region</th>\n",
       "      <th>Total_Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>2024-02-10</td>\n",
       "      <td>Monitor</td>\n",
       "      <td>1</td>\n",
       "      <td>20083</td>\n",
       "      <td>CUST041</td>\n",
       "      <td>West</td>\n",
       "      <td>20083</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>2024-01-27</td>\n",
       "      <td>Tablet</td>\n",
       "      <td>1</td>\n",
       "      <td>38298</td>\n",
       "      <td>CUST027</td>\n",
       "      <td>North</td>\n",
       "      <td>38298</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>2024-02-28</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>5</td>\n",
       "      <td>15475</td>\n",
       "      <td>CUST059</td>\n",
       "      <td>South</td>\n",
       "      <td>77375</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2024-01-13</td>\n",
       "      <td>Phone</td>\n",
       "      <td>8</td>\n",
       "      <td>20655</td>\n",
       "      <td>CUST013</td>\n",
       "      <td>East</td>\n",
       "      <td>165240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>72</th>\n",
       "      <td>2024-03-13</td>\n",
       "      <td>Headphones</td>\n",
       "      <td>7</td>\n",
       "      <td>49930</td>\n",
       "      <td>CUST073</td>\n",
       "      <td>West</td>\n",
       "      <td>349510</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Date     Product  Quantity  Price Customer_ID Region  Total_Sales\n",
       "40  2024-02-10     Monitor         1  20083     CUST041   West        20083\n",
       "26  2024-01-27      Tablet         1  38298     CUST027  North        38298\n",
       "58  2024-02-28      Laptop         5  15475     CUST059  South        77375\n",
       "12  2024-01-13       Phone         8  20655     CUST013   East       165240\n",
       "72  2024-03-13  Headphones         7  49930     CUST073   West       349510"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0af1f93e-2c78-4e20-95a5-5b68becc5969",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Price</th>\n",
       "      <th>Total_Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>100.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.780000</td>\n",
       "      <td>25808.510000</td>\n",
       "      <td>123650.480000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.588163</td>\n",
       "      <td>13917.630242</td>\n",
       "      <td>100161.085275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1308.000000</td>\n",
       "      <td>6540.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.750000</td>\n",
       "      <td>14965.250000</td>\n",
       "      <td>39517.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>24192.000000</td>\n",
       "      <td>97955.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.000000</td>\n",
       "      <td>38682.250000</td>\n",
       "      <td>175792.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.000000</td>\n",
       "      <td>49930.000000</td>\n",
       "      <td>373932.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Quantity         Price    Total_Sales\n",
       "count  100.000000    100.000000     100.000000\n",
       "mean     4.780000  25808.510000  123650.480000\n",
       "std      2.588163  13917.630242  100161.085275\n",
       "min      1.000000   1308.000000    6540.000000\n",
       "25%      2.750000  14965.250000   39517.500000\n",
       "50%      5.000000  24192.000000   97955.500000\n",
       "75%      7.000000  38682.250000  175792.500000\n",
       "max      9.000000  49930.000000  373932.000000"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "147b5e43-c348-46a4-ba1a-98aa9c79d495",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date           0\n",
       "Product        0\n",
       "Quantity       0\n",
       "Price          0\n",
       "Customer_ID    0\n",
       "Region         0\n",
       "Total_Sales    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7f1afd9d-7237-428b-b821-3ccf8e28645e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0900435b-85c2-4f3d-abfe-cb9f4830dec0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date           object\n",
       "Product        object\n",
       "Quantity        int64\n",
       "Price           int64\n",
       "Customer_ID    object\n",
       "Region         object\n",
       "Total_Sales     int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b44eb60a-b4a9-4368-984b-a5f895c5fb77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(12365048)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Metric 1: Total Sales\n",
    "total_sales = df['Total_Sales'].sum()\n",
    "total_sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "76f19a24-cced-4589-9ffb-4f7f1c21bb51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Product\n",
       "Laptop        3889210\n",
       "Tablet        2884340\n",
       "Phone         2859394\n",
       "Headphones    1384033\n",
       "Monitor       1348071\n",
       "Name: Total_Sales, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Metric 2: Best-Selling Product\n",
    "best_product= df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)\n",
    "best_product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "de62ea59-a5e0-4914-84ab-63b370579a88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(123650.48)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Average Sales per Transaction\n",
    "avg_sales = df['Total_Sales'].mean()\n",
    "avg_sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3a6db240-4053-49d4-aa67-338e3992af1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "373932"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Highest single sale:\n",
    "df['Total_Sales'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f6763bb9-78f2-4ead-8a5b-af3df40214e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6540"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Lowest single sale:\n",
    "df['Total_Sales'].min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5145f692-470c-4825-a6b1-9d029f2397c1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
