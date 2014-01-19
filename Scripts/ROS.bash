#Where catkin_ws is name of workspace
mkdir -p /vagrant/catkin_ws/src
cd /vagrant/catkin_ws/src
ls -la
cd ..
catkin_make
source devel/setup.bash
#catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp

