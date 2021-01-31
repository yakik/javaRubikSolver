/***************************************************************************
                          Face.cpp  -  description
                             -------------------
    begin                : Sat Apr 14 2001
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
#include "Face.h"

short oppositeFace(int p_face)
{                                          	
	switch (p_face)
	{
		case L: return R;
		case R: return L;
		case U: return D;
		case D: return U;
		case F: return B;
		case B: return F;
		default: return U;
	}			
}

short oppositeDirection(int p_direction)
{                                          	
	if (p_direction == CW)
		return CCW;
	else
		return CW;
}

char getFaceChar(int p_face)
{
	char l_returnValue;
	if (p_face == U)
		l_returnValue = 'U';		
	if (p_face == D)
		l_returnValue = 'D';		
	if (p_face == F)
		l_returnValue = 'F';		
	if (p_face == B)
		l_returnValue = 'B';		
	if (p_face == R)
		l_returnValue = 'R';		
	if (p_face == L)
		l_returnValue = 'L';		
	return l_returnValue;
}

char getDirectionChar(int p_direction)
{
	char l_returnValue;
	if (p_direction == CW)
		l_returnValue = 'C';		
	if (p_direction == CCW)
		l_returnValue = 'W';		
	return l_returnValue;
}

short getCharFace(char p_char)
{
	short l_returnValue=U;
	if (p_char == 'U')
		l_returnValue = U;		
	if (p_char == 'D')
		l_returnValue = D;		
	if (p_char == 'F')
		l_returnValue = F;		
	if (p_char == 'B')
		l_returnValue = B;		
	if (p_char == 'R')
		l_returnValue = R;		
	if (p_char == 'L')
		l_returnValue = L;		
	return l_returnValue;
}

short getCharDirection(char p_char)
{
	short l_returnValue=CW;
	if (p_char == 'C')
		l_returnValue = CW;
	if (p_char == 'W')
		l_returnValue = CCW;		
	return l_returnValue;
}
