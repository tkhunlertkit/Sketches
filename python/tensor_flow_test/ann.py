"""
    Sketch ideas for tensorflow study
"""
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

def nn():
    """
    Overall idea:
    NN with  784  ->   300  ->   10
            input -> hidden -> output
    using the provided mnist data
    """
    # mnist is a data of hand written image of 28 * 28 in greyscale.
    # The data contains 55000 training, 10000 testing, and 5000 validating samples
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

    #########################
    ##### NN parameters #####
    #########################
    learning_rate = 0.5
    epochs = 10
    batch_size = 100

    ############################
    ##### Input and output #####
    ############################
    x = tf.placeholder(tf.float32, [None, 784]) # Flatten values of hand written images (784 = 28 * 28)
    y = tf.placeholder(tf.float32, [None, 10])  # output values with 1 at the correct node number

    ###############################
    ###### Hiddenhidden layer #####
    ###############################
    # input to hidden layer
    w1 = tf.Variable(tf.random_normal([784, 300], stddev=0.3), name='ww1')
    b1 = tf.Variable(tf.random_normal([300]), name='bb1')
    # hidden to output
    w2 = tf.Variable(tf.random_normal([300, 10], stddev=0.3), name='ww2')
    b2 = tf.Variable(tf.random_normal([10]), name='bb2')

    ####################################
    ##### Hidden Layer Calculation #####
    ####################################
    hidden_output = tf.add(b1, tf.matmul(x, w1))
    hidden_out = tf.nn.relu(hidden_output)

    #######################
    #### output nodes #####
    #######################
    y_raw = tf.nn.softmax(tf.add(tf.matmul(hidden_out, w2), b2))

    ################################
    ##### Backward Propagation #####
    ################################
    y_clipped = tf.clip_by_value(y_raw, 1e-10, 0.9999999)
    cross_entropy = -tf.reduce_mean(tf.reduce_sum(y * tf.log(y_clipped) + (1 - y) * tf.log(1 - y_clipped), axis=1))

    # Optimiser
    optimiser = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cross_entropy)

    init_op = tf.global_variables_initializer()

    correction_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_clipped, 1))
    accuracy = tf.reduce_mean(tf.cast(correction_prediction, tf.float32))

    ############################################
    ##### NN training and accuracy testing #####
    ############################################
    with tf.Session() as sess:
        sess.run(init_op)
        total_batch = int(len(mnist.train.labels) / batch_size)

        for epoch in range(epochs):
            avg_cost = 0

            for batch in range(total_batch):
                training_data, training_target = mnist.train.next_batch(batch_size=batch_size)
                _, c = sess.run([optimiser, cross_entropy],
                    feed_dict={
                        x: training_data,
                        y: training_target
                    })
                avg_cost += c / total_batch
            print("Epoch:", (epoch + 1), "cost =", "{:.3f}".format(avg_cost))

        print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))


if __name__ == '__main__':
    nn()