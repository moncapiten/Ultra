import numpy as np
ν = 40.968 #kHz
V = 1e-2 #m/s
V_sound = 343.4 #m/s
θ = np.pi/4 #

def doppler_relativistico(ν, V, V_sound, θ):
    β = V/V_sound
    γ = 1/np.sqrt(1-β**2)
    ν_prime = (1/γ)*ν*(1+β*np.cos(θ))
    X_grid = 20e-2 #m
    T_grid = X_grid/V
    ν_grid = 1/T_grid
    return ν_prime , ν_grid


def doppler_classico(ν, V, V_sound, θ):
    ν_prime = V_sound/(V+V_sound)*ν
    X_grid = 20e-2 #m
    T_grid = X_grid/V
    ν_grid = 1/T_grid
    return ν_prime , ν_grid

ν_prime, ν_grid = doppler_relativistico(ν, V, V_sound, θ)
dν = abs(ν - ν_prime)
print(f"∆ν = {dν*1e3:.2f}, ν_grid={ν_grid:.2f}, ∆ν/ν_grid={dν/ν_grid}")


ν_prime, ν_grid = doppler_classico(ν, V, V_sound, θ)
dν = abs(ν - ν_prime)
print(f"∆ν = {dν*1e3:.2f}, ν_grid={ν_grid:.2f}, ∆ν/ν_grid={dν/ν_grid}")







