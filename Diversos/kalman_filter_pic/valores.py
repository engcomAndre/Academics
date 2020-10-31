#-*- coding: utf-8 -*-

# kalman1.py
# written by Greg Czerniak (email is greg {aT] czerniak [dOt} info )
#
# Implements a single-variable linear Kalman filter.
#
# Note: This code is part of a larger tutorial "Kalman Filters for Undergrads"
# located at http://greg.czerniak.info/node/5.

# --------------------------------------------------------------------------------------------#
# OBS: ALGORITMO MODIFICADO POR ALYNNE FERREIRA E MATEUS RODRIGUES                            #
# quantidade de números, nome do arquivo com os valores verdadeiros, nome do arquivo com erro #
#                                                                                             #
# saída: voltagereal.txt, cannonreal.txt, in.h - arquivo de entrada (com erros)               #
# --------------------------------------------------------------------------------------------#

import random
import numpy
import pylab
import math

arqin = open('in.h','w')

def voltage():
  class Voltmeter:
    def __init__(self,_truevoltage,_noiselevel):
      self.truevoltage = _truevoltage
      self.noiselevel = _noiselevel
    def GetVoltage(self):
      return self.truevoltage
    def GetVoltageWithNoise(self):
      return random.gauss(self.GetVoltage(),self.noiselevel)

  numsteps = 800

  A    = numpy.matrix([1])# matriz de transicao de estado
  H    = numpy.matrix([1]) # matriz de observacao
  B    = numpy.matrix([0]) # matriz de controle
  Q    = numpy.matrix([0.00001]) # erro estimado no processo
  R    = numpy.matrix([0.1]) # erro estimado nas medidas
  xhat = numpy.matrix([3]) # estimativa inicial do estado
  P    = numpy.matrix([1]) # estimativa de covariância inicial

  voltmeter = Voltmeter(1.25,0.25)

  measuredvoltage = []
  truevoltage = []

  for i in range(numsteps):
      measured = voltmeter.GetVoltageWithNoise()
      measuredvoltage.append(measured)
      truevoltage.append(voltmeter.GetVoltage())
    
  #gravando em arquivos

  ## valores reais
  arq = open('voltagereal.txt','w')
  for i in range (len(measuredvoltage)):
          arq.write(str("1.25"))
          arq.write('\n')    
  arq.close()

  ## valores com erro
  for i in range (len(measuredvoltage)-1):
          arqin.write(str(round(measuredvoltage[i],2)))
          arqin.write(',')    
  arqin.write(str(round(measuredvoltage[i],2))) #último sem vírgula
 
############################################################################################################## 

# Simulates the classic physics problem of a cannon shooting a ball in a
# parabolic arc.  In addition to giving "true" values back, you can also ask
# for noisy values back to test Kalman filters.
def cannonball():
  class Cannon:
    #--------------------------------VARIABLES----------------------------------
    angle = 45 # The angle from the ground to point the cannon.
    muzzle_velocity = 100 # Muzzle velocity of the cannon.
    gravity = [0,-9.81] # A vector containing gravitational acceleration.
    # The initial velocity of the cannonball
    velocity = [muzzle_velocity*math.cos(angle*math.pi/180), muzzle_velocity*math.sin(angle*math.pi/180)]
    loc = [0,0] # The initial location of the cannonball.
    acceleration = [0,0] # The initial acceleration of the cannonball.
    #---------------------------------METHODS-----------------------------------
    def __init__(self,_timeslice,_noiselevel):
      self.timeslice = _timeslice
      self.noiselevel = _noiselevel
    def add(self,x,y):
      return x + y
    def mult(self,x,y):
      return x * y
    def GetX(self):
      return self.loc[0]
    def GetY(self):
      return self.loc[1]
    def GetXWithNoise(self):
      return random.gauss(self.GetX(),self.noiselevel)
    def GetYWithNoise(self):
      return random.gauss(self.GetY(),self.noiselevel)
    def GetXVelocity(self):
      return self.velocity[0]
    def GetYVelocity(self):
      return self.velocity[1]
    # Increment through the next timeslice of the simulation.
    def Step(self):
      # We're gonna use this vector to timeslice everything.
      timeslicevec = [self.timeslice,self.timeslice]
      # Break gravitational force into a smaller time slice.
      sliced_gravity = list(map(self.mult,self.gravity,timeslicevec))
      # The only force on the cannonball is gravity.
      sliced_acceleration = sliced_gravity
      # Apply the acceleration to velocity.
      self.velocity = list(map(self.add, self.velocity, sliced_acceleration))
      sliced_velocity = list(map(self.mult, self.velocity, timeslicevec ))
      # Apply the velocity to location.
      self.loc = list(map(self.add, self.loc, sliced_velocity))
      # Cannonballs shouldn't go into the ground.
      if self.loc[1] < 0:
        self.loc[1] = 0

  #=============================REAL PROGRAM START================================
  # Let's go over the physics behind the cannon shot, just to make sure it's
  # correct:
  # sin(45)*100 = 70.710 and cos(45)*100 = 70.710
  # vf = vo + at
  # 0 = 70.710 + (-9.81)t
  # t = 70.710/9.81 = 7.208 seconds for half
  # 14.416 seconds for full journey
  # distance = 70.710 m/s * 14.416 sec = 1019.36796 m

  timeslice = 0.1 # How many seconds should elapse per iteration?
  iterations = 800 # How many iterations should the simulation run for?
  # (notice that the full journey takes 14.416 seconds, so 145 iterations will
  # cover the whole thing when timeslice = 0.10)
  noiselevel = 30  # How much noise should we add to the noisy measurements?
  muzzle_velocity = 800 # How fast should the cannonball come out?
  angle = 45 # Angle from the ground.

  # These are arrays to store the data points we want to plot at the end.
  x = []
  y = []
  nx = []
  ny = []

  # Let's make a cannon simulation.
  c = Cannon(timeslice,noiselevel)

  speedX = muzzle_velocity*math.cos(angle*math.pi/180)
  speedY = muzzle_velocity*math.sin(angle*math.pi/180)

  # This is the state transition vector, which represents part of the kinematics.
  # 1, ts, 0,  0  =>  x(n+1) = x(n) + vx(n)
  # 0,  1, 0,  0  => vx(n+1) =        vx(n)
  # 0,  0, 1, ts  =>  y(n+1) =              y(n) + vy(n)
  # 0,  0, 0,  1  => vy(n+1) =                     vy(n)
  # Remember, acceleration gets added to these at the control vector.
  state_transition = numpy.matrix([[1,timeslice,0,0],[0,1,0,0],[0,0,1,timeslice],[0,0,0,1]])

  control_matrix = numpy.matrix([[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]])
  # The control vector, which adds acceleration to the kinematic equations.
  # 0          =>  x(n+1) =  x(n+1)
  # 0          => vx(n+1) = vx(n+1)
  # -9.81*ts^2 =>  y(n+1) =  y(n+1) + 0.5*-9.81*ts^2
  # -9.81*ts   => vy(n+1) = vy(n+1) + -9.81*ts
  control_vector = numpy.matrix([[0],[0],[0.5*-9.81*timeslice*timeslice],[-9.81*timeslice]])

  # After state transition and control, here are the equations:
  #  x(n+1) = x(n) + vx(n)
  # vx(n+1) = vx(n)
  #  y(n+1) = y(n) + vy(n) - 0.5*9.81*ts^2
  # vy(n+1) = vy(n) + -9.81*ts
  # Which, if you recall, are the equations of motion for a parabola.  Perfect.

  # Iterate through the simulation.
  for i in range(iterations):
      x.append(c.GetX())
      y.append(c.GetY())
      newestX = c.GetXWithNoise()
      newestY = c.GetYWithNoise()
      nx.append(newestX)
      ny.append(newestY)
      # Iterate the cannon simulation to the next timeslice.
      c.Step()

  arq = open('cannonreal.txt','w')
  for i in range (iterations):
    arq.write(str(round(y[i],2)))
    arq.write('\n')    
  arq.close()

  for i in range (iterations-1):
    arqin.write(str(round(ny[i],2)))
    arqin.write(',')
  arqin.write(str(round(ny[i],2))) # último sem vírgula
  
##############################################################################################################
  
def main():

  arqin.write('#ifndef _IN_H_\n')
  arqin.write('#define _IN_H_\n')
  arqin.write('#define NUM_AMS 800\n')
  arqin.write("float const DATA1[] = {")
  voltage()
  arqin.write("};\n")
  arqin.write("float const DATA2[] = {")
  cannonball()  
  arqin.write("};\n")
  arqin.write('#endif');
  arqin.close()
  
main()
