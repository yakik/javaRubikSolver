/***************************************************************************
                          Permutation.h  -  description
                             -------------------
    begin                : Fri Apr 20 2001
    copyright            : (C) 2001 by yaki koren
    email                : 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

class Rubik;
class CubicleData;
#ifndef __Permutation_H
#define __Permutation_H

#include "CubicleData.h"
#include "Rubik.h"

class Permutation
{
public:	

  Permutation(){c_cubicles = -1;}
  void load(FILE *p_file);
  void addCubicleData(CubicleData p_cubicleData);
  int isPartRubik(Rubik *p_rubik);
  int getDifferece(Rubik *p_rubik);
  int getCubicleCount(){return (c_cubicles+1);}
  CubicleData getCubicleData(int p_index){return c_cubicleData[p_index];}
  void print();
  int getValue(int p_onlyFirstFloor);
 	Permutation *getCopy();
	int operator ==(Permutation p_permutation);



private:
	CubicleData c_cubicleData[20];
	short c_cubicles;

};

#endif
