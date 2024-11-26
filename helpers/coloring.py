#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

colors_40 = ['#a9a9a9', '#2f4f4f', '#556b2f', '#a0522d', '#228b22', '#191970', '#8b0000', '#808000', '#4682b4', '#9acd32',
             '#20b2aa', '#00008b', '#32cd32', '#daa520', '#8fbc8f', '#800080', '#b03060', '#ff4500', '#ff8c00', '#6a5acd',
             '#ffff00', '#0000cd', '#00ff00', '#9402d3', '#ba55d3', '#dc143c', '#00bfff', '#f4a460', '#adff2f', '#ff00ff',
             '#1e90ff', '#f0e68c', '#fa8072', '#dda0dd', '#afeeee', '#98fb98', '#7fffd4', '#ffdab9', '#ff69b4', '#ffb6c1']

colors_80 = ['#696969', '#a9a9a9', '#d3d3d3', '#2f4f4f', '#556b2f', '#6b8e23', '#a0522d', '#2e8b57', '#228b22', '#7f0000',
             '#191970', '#006400', '#808000', '#483d8b', '#b22222', '#5f9ea0', '#778899', '#3cb371', '#bc8f8f', '#663399',
             '#008080', '#bdb76b', '#4682b4', '#d2691e', '#9acd32', '#20b2aa', '#cd5c5c', '#00008b', '#4b0082', '#32cd32',
             '#daa520', '#8fbc8f', '#800080', '#b03060', '#66cdaa', '#9932cc', '#ff4500', '#ff8c00', '#ffa500', '#ffd700',
             '#ffff00', '#c71585', '#0000cd', '#deb887', '#40e0d0', '#7fff00', '#00ff00', '#9400d3', '#ba55d3', '#00fa9a',
             '#00ff7f', '#4169e1', '#dc143c', '#00ffff', '#00bfff', '#f4a460', '#9370db', '#0000ff', '#adff2f', '#d8bfd8',
             '#b0c4de', '#ff7f50', '#ff00ff', '#db7093', '#fa8072', '#eee8aa', '#ffff54', '#6495ed', '#dda0dd', '#b0e0e6',
             '#ff1493', '#7b68ee', '#ffa07a', '#ee82ee', '#98fb98', '#87cefa', '#7fffd4', '#ffdab9', '#ff69b4', '#ffc0cb']

default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

colorblind = sns.color_palette("colorblind", 9).as_hex()
colorblind_hex_codes = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161', '#fbafe4', '#949494', '#ece133']

linestyles = ['-', ':', '--']


def display_colors(colors_list):

    num_colors = len(colors_list)

    cmap = ListedColormap(colors_list)
    vals = range(len(colors_list))
    bounds = np.append(vals, vals[-1] + 1)
    norm = BoundaryNorm(bounds, ncolors=num_colors)

    fig, ax = plt.subplots(figsize=(0.35 * num_colors, 1))
    fig.subplots_adjust(bottom=0.5)
    fig.colorbar(ScalarMappable(norm=norm, cmap=cmap),
                 cax=ax, orientation='horizontal')

    for i in range(num_colors):
        ax.text(i + 0.35 / 2, 0.5, i)

    ax.axes.get_xaxis().set_visible(False)

    plt.show()
