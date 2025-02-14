import sys

sys.path.append("..")

from oppgave5.index import oppgave5
from utils.utils import get_h

import numpy as np
import pickle


def save_data(X_0, omega_0, n, interval, filename, drop_energy=False):
    """
    Denne funksjonen brukes til å lagre data om t-nøkkelen som senere skal brukes til å animere dem
    :param X_0: initialverdi til X.
    :param omega_0: vinkelhastighet ved tidspunkt 0
    :param n: antall steg.
    :param interval: start og sluttidspunkt for beregningen
    :param filename: filnavnet vi vil lagre dataen i
    :return none:
    """
    W, t, _, E = oppgave5(X_0, omega_0, n, interval, drop_energy=drop_energy)
    pickle.dump([W, t, E], open(f"data/{filename}", "wb"))


def load_data(filename):
    """
    denne filen leser data om t-nøkkelen fra en fil slik at vi kan animere dem
    :param filename: filnavnet vi skal lese data fra
    """
    data = pickle.load(open(f"data/{filename}", "rb"))
    return (
        np.array(data[0]["rk45"], dtype=np.double),
        np.array(data[0]["rk4"], dtype=np.double),
        np.array(data[0]["euler"], dtype=np.double),
        np.array(data[1]["rk45"], dtype=np.double),
        np.array(data[1]["rk4"], dtype=np.double),
        np.array(data[1]["euler"], dtype=np.double),
        np.array(data[2], dtype=np.double),
    )


if __name__ == "__main__":
    n = 200
    interval = [0.0, 100.0]
    X_0 = np.identity(3, dtype=np.double)

    omega_0_a = np.array([[1, 0.05, 0]], dtype=np.double).T
    save_data(X_0, omega_0_a, n, interval, "oppgavea.npy", drop_energy=True)

    omega_0_b = np.array([[0, 1.0, 0.05]], dtype=np.double).T
    save_data(X_0, omega_0_b, n, interval, "oppgaveb.npy")

    omega_0_c = np.array([[0.05, 0.0, 1.0]], dtype=np.double).T
    save_data(X_0, omega_0_c, n, interval, "oppgavec.npy")
