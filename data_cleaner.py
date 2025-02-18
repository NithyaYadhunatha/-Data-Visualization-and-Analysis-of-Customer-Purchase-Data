import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class DataCleaner:
    def __init__(self, file_path):
        try:
            self.df = pd.read_excel(file_path) if 'xlsx' in file_path else pd.read_csv(file_path)
            self.original_df = self.df.copy()
        except Exception as e:
            print(f"Error reading file: {e}")
            self.df = pd.DataFrame()

    def clean(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            if 'age' in col.lower():
                self.df = self.df[self.df[col].between(18, 100)]
            elif 'purchase' in col.lower():
                self.df = self.df[self.df[col] > 0]
            elif 'income' in col.lower():
                self.df[col].fillna(self.df[col].median(), inplace=True)
        
        self.df.drop_duplicates(inplace=True)
        return self

    def visualize(self, output_dir='./output'):
        os.makedirs(output_dir, exist_ok=True)
        plt.figure(figsize=(20, 15))

        numeric_cols = self.df.select_dtypes(include=['number']).columns
        category_col = self.df.select_dtypes(include=['object']).columns[0] if len(self.df.select_dtypes(include=['object']).columns) > 0 else None

        # Purchase Amount Distribution
        purchase_col = next((col for col in numeric_cols if 'purchase' in col.lower()), None)
        if purchase_col:
            plt.subplot(2, 2, 1)
            sns.histplot(self.df[purchase_col], kde=True)
            plt.title('Distribution of Purchase Amounts')

        # Box Plot 
        if category_col and purchase_col:
            plt.subplot(2, 2, 2)
            sns.boxplot(x=category_col, y=purchase_col, data=self.df)
            plt.title('Purchase Amount by Category')
            plt.xticks(rotation=45)

        # Scatter Plot
        age_col = next((col for col in numeric_cols if 'age' in col.lower()), None)
        income_col = next((col for col in numeric_cols if 'income' in col.lower()), None)
        if age_col and purchase_col and income_col:
            plt.subplot(2, 2, 3)
            scatter = plt.scatter(self.df[age_col], self.df[purchase_col], 
                                  c=self.df[income_col], cmap='viridis', alpha=0.6)
            plt.title('Age vs Purchase Amount')
            plt.colorbar(scatter, label='Income')

        # Pie Chart
        if category_col:
            plt.subplot(2, 2, 4)
            category_counts = self.df[category_col].value_counts()
            plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
            plt.title('Category Distribution')

        plt.suptitle('Data Visualization Dashboard')
        plt.tight_layout()
        
        
    def report(self):
        print("\n--- Data Report ---")
        print(f"Original Dataset Size: {len(self.original_df)}")
        print(f"Cleaned Dataset Size: {len(self.df)}")
        
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print("\nKey Statistics:")
        print(self.df[numeric_cols].describe())
        return self

def main():
    file_path = r'C:\Users\ynith\OneDrive\Desktop\Nithya\sample_customer_data.csv'
    (DataCleaner(file_path)
     .clean()
     .report()
     .visualize())

if __name__ == "__main__":
    main()
