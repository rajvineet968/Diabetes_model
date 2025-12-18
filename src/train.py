import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def main():
    # MLflow setup for CI
    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("ci_cd_training")

    # Load sample data (CI-safe)
    X, y = load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=50, random_state=42)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)

        mlflow.log_param("model", "RandomForest")
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

        print("Training completed. MSE:", mse)

if __name__ == "__main__":
    main()
