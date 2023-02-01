# show kinetic energy
def kinetic_energy(mass, velocity):
    kin_energy = (mass * velocity ** 2) / 2
    return kin_energy


def main():
    # get mass and velocity values from user
    mass = float(input('Enter body mass in kg: '))
    velocity = float(input('Enter body speed in m/s: '))

    # get kinetic enegry
    kin_energy = kinetic_energy(mass, velocity)
    print(f"Kinetic energy of body is {kin_energy}")


main()
