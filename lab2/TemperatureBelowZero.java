import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.api.common.functions.FilterFunction;

public class TemperatureBelowZero {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env =
            StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<Temperature> temperatures = env.fromElements(
            new Temperature("Sensor 1", 4),
            new Temperature("Sensor 2", -3),
            new Temperature("Sensor 3", 12),
            new Temperature("Sensor 4", -8)
        );

        DataStream<Temperature> belowZero = temperatures.filter(new FilterFunction<Temperature>() {
            @Override
            public boolean filter(Temperature temperature) throws Exception {
                return temperature.value < 0;
            }
        });

        belowZero.print();
        env.execute();
    }

    public static class Temperature {
        public String sensor;
        public Integer value;

        public Temperature() {}

        public Temperature(String sensor, Integer value) {
            this.sensor = sensor;
            this.value = value;
        }

        public String toString() {
            return this.sensor.toString() + ": temperature " + this.value.toString() + " C";
        }
    }
}
