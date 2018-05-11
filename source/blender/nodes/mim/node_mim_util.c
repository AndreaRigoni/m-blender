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

/** \file blender/nodes/shader/node_shader_util.c
 *  \ingroup nodes
 */


#include "DNA_node_types.h"
#include "node_shader_util.h"

#include "node_exec.h"


int mim_node_poll_default(bNodeType *UNUSED(ntype), bNodeTree *ntree)
{
    return STREQ(ntree->idname, "MimNodeTree");
}

void mim_node_type_base(struct bNodeType *ntype, int type, const char *name, short nclass, short flag)
{
	node_type_base(ntype, type, name, nclass, flag);
	
    ntype->poll = mim_node_poll_default;
	ntype->insert_link = node_insert_link_default;
	ntype->update_internal_links = node_update_internal_links_default;
}

