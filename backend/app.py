"""
Datalyze - Simple CSV Processing Module

Database storage is handled by FastAPI routes using SQLAlchemy models.
"""

import pandas as pd
from pathlib import Path
from typing import Optional, Dict, Any


class DatalyzeApp:
    """Simple CSV processing handler"""
    
    def __init__(self, upload_dir: str = "uploads"):
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(exist_ok=True)
    
    def save_file(self, file_path: str, saved_filename: str) -> str:
        """
        Copy file to uploads directory
        Returns the path where file was saved
        """
        import shutil
        dest_path = self.upload_dir / saved_filename
        shutil.copy2(file_path, dest_path)
        return str(dest_path)
    
    def load_csv(self, file_path: str) -> pd.DataFrame:
        """Load CSV file from path"""
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        return df
    
    def analyze_data(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Basic data analysis"""
        analysis = {
            "rows": int(len(df)),
            "columns": int(len(df.columns)),
            "column_names": list(df.columns),
            "missing_values": {col: int(count) for col, count in df.isnull().sum().items()},
            "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "memory_mb": float(df.memory_usage(deep=True).sum() / 1024 / 1024)
        }
        return analysis
    
    def get_column_stats(self, df: pd.DataFrame, column: str) -> Dict[str, Any]:
        """Get statistics for a specific column"""
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        series = df[column]
        stats = {
            "name": column,
            "dtype": str(series.dtype),
            "count": int(series.count()),
            "missing": int(series.isnull().sum()),
            "unique": int(series.nunique())
        }
        
        # Add numeric stats if applicable
        if pd.api.types.is_numeric_dtype(series):
            stats["mean"] = float(series.mean())
            stats["median"] = float(series.median())
            stats["std"] = float(series.std())
            stats["min"] = float(series.min())
            stats["max"] = float(series.max())
        
        return stats
    
    def detect_delimiter(self, file_path: str) -> str:
        """Auto-detect CSV delimiter"""
        with open(file_path, 'r') as f:
            first_line = f.readline()
        
        delimiters = [',', '\t', ';', '|']
        counts = {d: first_line.count(d) for d in delimiters}
        return max(counts, key=counts.get)
    
    def validate_csv(self, file_path: str) -> Dict[str, Any]:
        """Validate CSV file"""
        try:
            df = pd.read_csv(file_path, nrows=5)
            return {
                "valid": True,
                "rows_sample": len(df),
                "columns": len(df.columns)
            }
        except Exception as e:
            return {
                "valid": False,
                "error": str(e)
            }
    
    def get_preview(self, file_path: str, rows: int = 10) -> Dict[str, Any]:
        """Get file preview"""
        df = self.load_csv(file_path)
        
        return {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "data": df.head(rows).to_dict(orient='records')
        }
    
    def clean_data(self, df: pd.DataFrame, drop_duplicates: bool = False, 
                   drop_na: bool = False) -> pd.DataFrame:
        """Basic data cleaning"""
        df_clean = df.copy()
        
        if drop_duplicates:
            df_clean = df_clean.drop_duplicates()
        
        if drop_na:
            df_clean = df_clean.dropna()
        
        return df_clean
    
    def get_correlation_matrix(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Get correlation matrix for numeric columns"""
        numeric_cols = df.select_dtypes(include=['number']).columns
        
        if len(numeric_cols) < 2:
            return {"error": "Not enough numeric columns for correlation"}
        
        corr_matrix = df[numeric_cols].corr()
        return corr_matrix.to_dict()


# Global instance
app = DatalyzeApp()


# Simple functions for API routes to use
def save_uploaded_file(file_path: str, saved_filename: str) -> str:
    """Save uploaded file and return saved path"""
    return app.save_file(file_path, saved_filename)


def load_csv_file(file_path: str) -> pd.DataFrame:
    """Load CSV file"""
    return app.load_csv(file_path)


def analyze_csv(file_path: str) -> Dict[str, Any]:
    """Analyze CSV file"""
    df = app.load_csv(file_path)
    return app.analyze_data(df)


def get_csv_preview(file_path: str, rows: int = 10) -> Dict[str, Any]:
    """Get CSV preview"""
    return app.get_preview(file_path, rows)


def validate_csv_file(file_path: str) -> Dict[str, Any]:
    """Validate CSV file"""
    return app.validate_csv(file_path)


def get_column_statistics(file_path: str, column: str) -> Dict[str, Any]:
    """Get statistics for a column"""
    df = app.load_csv(file_path)
    return app.get_column_stats(df, column)


def get_correlations(file_path: str) -> Dict[str, Any]:
    """Get correlation matrix"""
    df = app.load_csv(file_path)
    return app.get_correlation_matrix(df)