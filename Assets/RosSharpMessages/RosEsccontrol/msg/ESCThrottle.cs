/* 
 * This message is auto generated by ROS#. Please DO NOT modify.
 * Note:
 * - Comments from the original code will be written in their own line 
 * - Variable sized arrays will be initialized to array of size 0 
 * Please report any issues at 
 * <https://github.com/siemens/ros-sharp> 
 */

using Newtonsoft.Json;

namespace RosSharp.RosBridgeClient.MessageTypes.RosEsccontrol
{
    public class ESCThrottle : Message
    {
        [JsonIgnore]
        public const string RosMessageName = "ros_esccontrol/ESCThrottle";

        public int motor_num;
        public float power;

        public ESCThrottle()
        {
            this.motor_num = 0;
            this.power = 0.0f;
        }

        public ESCThrottle(int motor_num, float power)
        {
            this.motor_num = motor_num;
            this.power = power;
        }
    }
}
