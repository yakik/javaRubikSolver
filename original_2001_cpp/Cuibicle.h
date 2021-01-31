/***************************************************************************
                          Cuibicle.h  -  description
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
#ifndef __Cubicle_H
#define __Cubicle_H


class cubicle
{
public:
		int cubieInHomeLocation();
		int cubieInHomePosition();
		Cubie getHomeCubie();
		Cubie getCubie();
void rotateHorizonalViewpoint(Direction p_direction);
		void rotateVerticalViewpoint(Direction p_direction);
		void rotateFace(Face p_face, Direction p_direction);
		void printViewpointFace();
private:
		Cuibcle c_cubicles[3][3][3];
		Face 		c_frontViewPoint;
		Face		c_top_ViewPoint;
};

#endif
