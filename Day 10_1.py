import pathlib
import re
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

dataR = re.compile("position=<([- 0-9]+), ([- 0-9]+)> velocity=<([- 0-9]+), ([- 0-9]+)>")
data = [list(map(int, dataR.search(line).groups())) for line in pathlib.Path("inputs/10.txt").read_text().splitlines()]

data = tf.constant(np.array(data), dtype=np.float32)
pos = data[:, :2]
vel = data[:, 2:]
time = tf.placeholder_with_default(tf.Variable(0.0), shape=())
finalPos = pos + vel * time

_, variance = tf.nn.moments(finalPos, axes=[0])
loss = tf.reduce_sum(variance)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    prevVals = None
    while True:
        _, lossVal, timeVal = sess.run((train_op, loss, time))
        lossVal = round(lossVal, 1)
        timeVal = round(timeVal)
        if prevVals == (lossVal, timeVal):
            break
        prevVals = (lossVal, timeVal)
    finalPosVal = sess.run(finalPos, feed_dict={time: timeVal})

finalPosVal = finalPosVal.astype(np.int32)
finalPosVal[:, 0] -= np.min(finalPosVal[:, 0])
finalPosVal[:, 1] -= np.min(finalPosVal[:, 1])

image = np.ones(shape=(max(finalPosVal[:, 1]) + 1, max(finalPosVal[:, 0]) + 1), dtype=np.int32)
for x, y in finalPosVal:
    image[y, x] = 0

plt.imshow(image, cmap="gray")
plt.show()
