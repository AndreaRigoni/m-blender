/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version. 
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2005 Blender Foundation.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): none yet.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file blender/nodes/mim/node_mim_util.h
 *  \ingroup nodes
 */


#ifndef __NODE_MIM_UTIL_H__
#define __NODE_MIM_UTIL_H__

#include <math.h>
#include <float.h>
#include <string.h>

#include "MEM_guardedalloc.h"

#include "DNA_color_types.h"
#include "DNA_customdata_types.h"
#include "DNA_ID.h"
#include "DNA_image_types.h"
#include "DNA_material_types.h"
#include "DNA_node_types.h"
#include "DNA_object_types.h"
#include "DNA_scene_types.h"
#include "DNA_texture_types.h"

#include "BLI_math.h"
#include "BLI_blenlib.h"
#include "BLI_rand.h"
#include "BLI_threads.h"
#include "BLI_utildefines.h"

#include "BKE_colorband.h"
#include "BKE_colortools.h"
#include "BKE_global.h"
#include "BKE_image.h"
#include "BKE_main.h"
#include "BKE_node.h"

#include "BKE_library.h"

#include "node_util.h"


int mim_node_poll_default(struct bNodeType *ntype, struct bNodeTree *ntree);
void mim_node_type_base(struct bNodeType *ntype, int type, const char *name, short nclass, short flag);



typedef struct MimCallData {
	/* Empty for now, may be reused if we convert shader to texture nodes. */
	int dummy;
} MimCallData;

void nodestack_get_vec(float *in, short type_in, bNodeStack *ns);


#endif
