/***************************************************************************
                          CubicleData.h  -  description
                             -------------------
    begin                : Thu Apr 12 2001
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
#ifndef __CubicleData_H
#define __CubicleData_H

#include "Position.h"
#include "Location.h"


class CubicleData
{
public:	
	
  CubicleData(){}
	CubicleData(Location p_location, Location p_cubieLocation, Position p_cubiePosition);
  Location getLocation(){return c_location;}
	Location getCubieLocation(){return c_cubieLocation;}
	Position getCubiePosition(){return c_cubiePosition;}
	int operator ==(CubicleData p_cubicleData);

private:
	Location c_location;
	Location c_cubieLocation;
	Position c_cubiePosition;
};

#endif
