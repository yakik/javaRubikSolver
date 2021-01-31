
/***************************************************************************
                          perspectives.cpp  -  description
                             -------------------
    begin                : Mon Apr 9 2001
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
#include "Position.h"





void Position::rotate(Rotation p_rotation)
{
  int l_temp;
  int l_face = p_rotation.getFace();
  int l_direction = p_rotation.getDirection();
  if (l_face == U)
		if (l_direction == CW)
			c_currentFront=getFace(R);
		else
			c_currentFront=getFace(L);
	else
		if (l_face == R)
 			if (l_direction == CW)
			{
				l_temp = c_currentFront;
				c_currentFront=getFace(D);
				c_currentUp = l_temp;
			}
			else
			{
				l_temp = getFace(B);
				c_currentFront = c_currentUp;
				c_currentUp = l_temp;
			}
		else
			if (l_face == F)
				if (l_direction == CW)
					c_currentUp=getFace(L);
				else
					c_currentUp=getFace(R);
			else
        rotate(Rotation(oppositeFace(l_face),oppositeDirection(l_direction)));

}


int Position::getFace(int p_viewpoint)
{
	if (p_viewpoint == U)
		return c_currentUp;
	else
		if (p_viewpoint == D)
			return oppositeFace(c_currentUp);
		else
			return getHorizonalFacebyVirtual(p_viewpoint);
}


int Position::getHorizonalFacebyVirtual(int p_viewpoint)
{
int i=0;

while (g_faceOrder[c_currentUp][i]!=c_currentFront && i<4)
	i++;
switch (p_viewpoint)
	{
	case F: return  g_faceOrder[c_currentUp][i];break;
	case L: return  g_faceOrder[c_currentUp][(i+1)%4];break;
	case B: return  g_faceOrder[c_currentUp][(i+2)%4];break;
	case R: return  g_faceOrder[c_currentUp][(i+3)%4];break;
	default: return U; break;
	}
}

int Position::operator ==(Position p_position)
	{
		return ((c_currentUp == p_position.c_currentUp) &&
			 			(c_currentFront == p_position.c_currentFront));
	}
	
	int Position::operator !=(Position p_position)
	{
		return !(operator==(p_position));
	}

