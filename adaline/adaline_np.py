import numpy as np


def activation_function(x: np.ndarray) -> np.ndarray:
    """
    Função de ativação do AdaLine. Como o AdaLine trabalha com regressão linear,
    a ativação é simplesmente a função identidade (f(x) = x).
    """
    return x


def initialize_weights(n_features: int) -> np.ndarray:
    """
    Inicializa os pesos aleatoriamente com valores pequenos.
    :param n_features: Número de características (features) do dataset
    :return: Vetor de pesos inicializado
    """
    return np.random.randn(n_features + 1) * 0.01


def predict(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Realiza a predição para um conjunto de entrada X, dado um vetor de pesos.
    :param X: Matriz de entrada (amostras x features)
    :param weights: Vetor de pesos
    :return: Vetor de predições
    """
    X_bias = np.c_[np.ones(X.shape[0]), X]
    return activation_function(X_bias @ weights)


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calcula o erro quadrático médio entre os valores verdadeiros e as predições.
    :param y_true: Valores verdadeiros
    :param y_pred: Valores preditos pelo modelo
    :return: Valor do erro quadrático médio
    """
    return np.mean((y_true - y_pred) ** 2)


def update_weights(X: np.ndarray, y: np.ndarray, weights: np.ndarray, lr: float) -> np.ndarray:
    """
    Atualiza os pesos do modelo usando o gradiente da MSE.
    :param X: Matriz de entrada (amostras x features)
    :param y: Vetor de valores reais
    :param weights: Vetor de pesos atual
    :param lr: Taxa de aprendizado
    :return: Vetor de pesos atualizado
    """
    X_bias = np.c_[np.ones(X.shape[0]), X]
    y_pred = predict(X, weights)
    gradient = -2 * (X_bias.T @ (y - y_pred)) / X.shape[0]
    return weights - lr * gradient


def train(X: np.ndarray, y: np.ndarray, epochs: int = 100, lr: float = 0.01) -> np.ndarray:
    """
    Treina o modelo AdaLine por um número de épocas usando o gradiente descendente.
    :param X: Matriz de entrada (amostras x features)
    :param y: Vetor de valores reais
    :param epochs: Número de épocas de treinamento
    :param lr: Taxa de aprendizado
    :return: Vetor de pesos treinado
    """
    weights = initialize_weights(X.shape[1])
    for _ in range(epochs):
        weights = update_weights(X, y, weights, lr)
    return weights
