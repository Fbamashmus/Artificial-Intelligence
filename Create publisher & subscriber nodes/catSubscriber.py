import rospy
from std_msgs.msg import String
def callback_str(data):
	rospy.loginfo(data.data)
def cat_listenr():
	#hello_pub = rospy.Publisher('hello', String, queue_size=10)
	rospy.init_node('cat', anonymous=False)
	rospy.Subscriber('hello',String, callback_str)
	rospy.spin()
	

if __name__== '__main__':
	cat_listenr()

