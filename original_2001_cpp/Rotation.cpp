/***************************************************************************
                          Rotation.cpp  -  description
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
#include "Rotation.h"
  Rotation::Rotation(int p_face, int p_direction)
  {
  	c_face = p_face;
  	c_direction = p_direction;
  }

  int Rotation::reset(FILE *p_file)
  {
		char l_char;
		l_char = fgetc(p_file);
		while ((l_char == ' '))
			l_char = fgetc(p_file);		
		if ((l_char=='\n')||(l_char==EOF)||(l_char!='('))
			return 0;
		else
		{
			int l_tempInt;
			fscanf(p_file,"%d",&l_tempInt);
			c_face = l_tempInt;
			fgetc(p_file);
			fscanf(p_file,"%d",&l_tempInt);
			c_direction = l_tempInt;
			fgetc(p_file);
			return 1;
		}
	}
			

  Rotation::Rotation(int p_value)
  {
  	if (p_value > 5)
  	{
  		c_direction = 1;
  		c_face = p_value - 6;
  	}
  	else
  	{
  		c_direction = 0;
  		c_face = p_value;
  	}
  }

  int Rotation::getValue()
  {
  	return (c_face + c_direction*6);
  }

  int Rotation::getFace()
  {
  	return c_face;
  }

  int Rotation::getDirection()
  {
  	return c_direction;
  }

  void Rotation::print()
  {
  	printf("(%c,%c)", getFaceChar(c_face), getDirectionChar(c_direction));
  }

  Rotation Rotation::getReverse()
  {
  	return Rotation(c_face, oppositeDirection(c_direction));
  }

  int Rotation::operator ==(Rotation p_rotation)
	{
		return ((c_face == p_rotation.c_face) &&
			 			(c_direction == p_rotation.c_direction));
	}
