##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *

class Splinelib(CMakePackage):
    """Library for spline manipulation."""

    homepage = "http://www.cats.rwth-aachen.de"
    url = ""

    version('rwthdevelop', git='git.rwth-aachen.de:splinelibpp/splinelib.git', branch='develop')

    variant('cpp', default=True, description='Compile witch C++ interface.')
    variant('coverage', default=False, description='Compile with coverage support.')

    depends_on("boost", when='+cpp')
    depends_on("googletest+gmock", when='+cpp')

    def cmake_args(self):
        options = []
        spec = self.spec

        options.extend([
            '-DSPLINELIB_CPP_API=%s' % (
                'ON' if '+cpp' in spec else 'OFF'),
            '-DSPLINELIB_COVERAGE=%s' % (
                'ON' if '+coverage' in spec else 'OFF')
            ])

        return options
