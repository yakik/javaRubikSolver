/***************************************************************************
                          Face.h  -  description
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
#ifndef __Face_H
#define __Face_H

	enum Direction {CW,CCW};
	enum Face {U,D,R,L,F,B}; //don't change this sequence, for Rubik's sake!
	const Face g_faceOrder[6][4]={{F,L,B,R},{R,B,L,F},{U,B,D,F},{U,F,D,B},{U,R,D,L},{U,L,D,R}};	
  char getFaceChar(int p_face);
  char getDirectionChar(int p_direction);
	short getCharFace(char p_char);
	short getCharDirection(char p_char);
	short oppositeFace(int p_face);
	short oppositeDirection(int p_direction);

#endif
