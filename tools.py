import numpy as np
import scipy as sp

# Constantes
c = 3e5  # Velocidad de la luz en km/s

# Función para H(z)
def H(z, H0, Omega_m0, Omega_lambda0):
    return H0 * np.sqrt(Omega_m0 * (1 + z)**3 + Omega_lambda0)
 
# Integrando de la distancia comóvil
def integrando(z, H0, Omega_m0, Omega_lambda0):
    return 1 / H(z, H0, Omega_m0, Omega_lambda0)
 
# Función para calcular la distancia comóvil
def distancia_comovil(z, H0, Omega_m0, Omega_lambda0):
    integral, _ = sp.integrate.quad(integrando, 0, z, args=(H0, Omega_m0, Omega_lambda0))
    return (c * integral)