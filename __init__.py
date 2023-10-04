# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SpatialDistributionPattern
                                 A QGIS plugin
 This plugin estimates the Spatial Distribution Pattern of point and linear features.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-08-14
        copyright            : (C) 2023 by Marconi Martins Cunha
        email                : marconi.cunha@ufv.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SpatialDistributionPattern class from file SpatialDistributionPattern.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SpatialDistributionPattern import SpatialDistributionPattern
    return SpatialDistributionPattern(iface)
