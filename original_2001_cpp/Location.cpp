/***************************************************************************
                          Lcation.cpp  -  description
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
#include "Location.h"


	Location::Location(int p_face0,int p_face1,int p_face2)
	{
		int l_tmp;
		c_isEdge = 0;
		c_face0 = p_face0;
		c_face1 = p_face1;
		c_face2 = p_face2;
// bubble sort to keep order within faces		
		if (c_face0 > c_face1)
		{
			l_tmp = c_face1;
			c_face1 = c_face0;
			c_face0 = l_tmp;
		}
		if (c_face1 > c_face2)
		{
			l_tmp = c_face2;
			c_face2 = c_face1;
			c_face1 = l_tmp;
		}
		if (c_face0 > c_face1)
		{
			l_tmp = c_face1;
			c_face1 = c_face0;
			c_face0 = l_tmp;
		}

	}
	
	Location::Location(int p_face0,int p_face1)
	{
		c_isEdge = 1;
		c_face2 = 9;
		c_face0 = p_face0;
		c_face1 = p_face1;
		if (p_face0>p_face1)
		{
			c_face1 = p_face0;
			c_face0 = p_face1;
		}
		else
		{
			c_face0 = p_face0;
			c_face1 = p_face1;
		}
	}
	
	int Location::isEdge()
	{
		return c_isEdge;
	}

  int Location::getFace0()
  {
  	return c_face0;
  }

  int Location::getFace1()
  {
  	return c_face1;
  }

  int Location::getFace2()
  {
  	if (isEdge())
			return 0;
		else
			return c_face2;
  }

	int Location::getValue()
	{
		return  (getFace0()*1+getFace1()*6+getFace2()*36+isEdge()*216);
	}
	
	int Location::operator ==(Location p_location)
	{
		return ((c_face0 == p_location.c_face0) &&
			 			(c_face1 == p_location.c_face1) &&
			 			(c_face2 == p_location.c_face2) &&
			 			(c_isEdge == p_location.c_isEdge));
	}
	
	int Location::operator !=(Location p_location)
	{
		return !(operator==(p_location));
	}
	
	void Location::print()
	{
		if (c_isEdge)
			printf("face0=%c, face1=%c",getFaceChar(c_face0),getFaceChar(c_face1));
		else
			printf("face0=%c, face1=%c, face2=%c",getFaceChar(c_face0),getFaceChar(c_face1),getFaceChar(c_face2));	}

