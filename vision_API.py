#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_quickstart():

    # [START vision_quickstart]

    shapes = [
        'triangle',
        'rectangle',
        'quadrilateral',
        'square',
        'rhombus',
        'ellipse',
        'oval',
        'circle',
        'polygon',
        'convex polygon',
        'concave polygon',
        'pentagon',
        'hexagon',
        'line',
        'point',
        'angle',
        'slope',
        'trapezium',
        ]
    best_description = [
        'venn diagram',
        'diagram',
        'plot',
        'graph',
        'chart',
        'set',
        'set notation',
        'function',
        'graph of function',
        'map',
        'relation',
        'union',
        'intersection',
        'vector',
        'symmetry',
        'piecewise linear function',
        'injective function',
        'surjective function',
        'sine wave',
        'cos wave',
        'quadratic function',
        'linear function'
        ]

    import io
    import os
    # save the images to be classified in .png format and place the names of the files in this list1
    list1 = [
        'b3',
        'b4',
        'b5',
        'b6',
        'b8',
        'b9',
        'b10',
        ]

    # Imports the Google Cloud client library
    # [START migration_import]

    from google.cloud import vision
    from google.cloud.vision import types

    # [END migration_import]

    # Instantiates a client
    # [START migration_client]

    for i in range(len(list1)):
        print 'Showing image analysis for ' + list1[i]
        print '---------------------------------------------------------------------'

        # [END migration_client]

        client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    # set the path of the image files here
        name = 'resources/' + list1[i] + '.png'
        file_name = os.path.join(os.path.dirname(__file__), name)

    # Loads the image into memory

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)

    # Performs label detection on the image file

    # Performs web entity detection on the image file
        probable_desc = []
        web_detection = client.web_detection(image=image).web_detection
        if web_detection.web_entities:
            print '\n{} Web entities found: '.format(len(web_detection.web_entities))
        max_score = 0
        best_desc = ''
        found_shapes = []
        for entity in web_detection.web_entities:
            for items in best_description:
                if items.lower() == entity.description.lower():
                    probable_desc.append(entity.description.lower())
        for entity in web_detection.web_entities:
            for items in best_description:
                if items.lower() == entity.description.lower() and max_score < float(entity.score):
                    print 1
                    max_score = float(entity.score)
                    best_desc = entity.description
                    if best_desc.lower() == 'function':
                            best_desc = 'graph of function'
            for items in shapes:
                if items.lower() == entity.description:
                    found_shapes.append(items.lower())

            print 'Score      : {}'.format(entity.score)
            print 'Description: {}'.format(entity.description)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print 'Labels:'
        flag = 0
        for label in labels:
            for items in shapes:
                if items.lower() == label.description:
                    found_shapes.append(items.lower())
            print label.description
        if best_desc == '':
            for label in labels:
                for items in best_description:
                    if items == label.description:
                        best_desc = label.description
                        if best_desc.lower() == 'function':
                            best_desc = 'graph of function'
                        flag = 1
                        break
                if flag == 1:
                    break
        print found_shapes
        print probable_desc
        if(best_desc != ''):
            print 'The image can be best described as a ' + best_desc.lower()
        shape_string = ''
        if(len(found_shapes) > 1):
            shape_string = 'The shapes found in this image are '
            for i in range(len(found_shapes) - 1):
                if(i != len(found_shapes)-2):
                    shape_string = shape_string + found_shapes[i] + ', '
                else:
                    shape_string = shape_string + found_shapes[i] + ' '
            shape_string = shape_string + 'and ' + found_shapes[len(found_shapes)-1] +'.'
        if(len(found_shapes) == 1):
            shape_string = 'The shape found in this image is '
            shape_string = shape_string + found_shapes[len(found_shapes)-1] +'.'
        print shape_string
        if(best_desc.lower() == 'plot'):
            print 'The ' + best_desc + ' consists of a x-axis and y-axis are perpendicular intersecting at origin O' 
        desc_string = ''
        if(len(probable_desc) > 1):
            desc_string = 'The image may also be described as '
            for i in range(len(probable_desc) - 1):
                if(i != len(probable_desc)-2):
                    desc_string = desc_string + probable_desc[i] + ' or '
                else:
                    desc_string = desc_string + probable_desc[i] + ' '
            desc_string = desc_string + 'or ' + probable_desc[len(probable_desc)-1] +'.'
        if(len(probable_desc) == 1):
            probable_desc = 'The image may also be described as '
            desc_string = desc_string + probable_desc[len(probable_desc)-1] +'.'
        print desc_string

        print '---------------------------------------------------------------------'
        print '---------------------------------------------------------------------'
        print '---------------------------------------------------------------------'


    # perform text detection on image file
        # [END vision_quickstart]

if __name__ == '__main__':
    run_quickstart()


			
