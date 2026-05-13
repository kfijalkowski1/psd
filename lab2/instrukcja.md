# Zajęcia zintegrowane 2

**2026L**

Celem zajęć zintegrowanych jest zapoznanie się z działaniem narzędzia Flink do
przetwarzania danych strumieniowych.

## Instrukcja

1. Uruchom przygotowaną maszynę wirtualną w VirtualBox.
2. Uruchom Flink:
- 
  ```bash
   cd flink-* && ls -l
  ```
Ścieżka do Flink może ulec zmianie w maszynie wirtualnej.
- `./bin/start-cluster.sh`
- ` ./bin/stop-cluster.sh` # to stop cluster
3. Uruchom testową aplikację Flink:
```bash
./bin/flink run examples/streaming/WordCount.jar
```
   Sprawdzenie poprawności uruchomienia:
```bash
tail log/flink-*-taskexecutor-*.out
```
4. Monitoruj działanie Flink z wykorzystaniem interfejsu WWW Flink:
  [http://localhost:8081/](http://localhost:8081/)
   Zinterpretuj otrzymane dane monitoringu.
5. Skompiluj i uruchom przykładowy program:
  ```java
   import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
   import org.apache.flink.streaming.api.datastream.DataStream;
   import org.apache.flink.api.common.functions.FilterFunction;

   public class Example {
       public static void main(String[] args) throws Exception {
           final StreamExecutionEnvironment env =
               StreamExecutionEnvironment.getExecutionEnvironment();

           DataStream<Person> flintstones = env.fromElements(
               new Person("Fred", 35),
               new Person("Wilma", 35),
               new Person("Pebbles", 2)
           );

           DataStream<Person> adults = flintstones.filter(new FilterFunction<Person>() {
               @Override
               public boolean filter(Person person) throws Exception {
                   return person.age >= 18;
               }
           });

           adults.print();
           env.execute();
       }

       public static class Person {
           public String name;
           public Integer age;

           public Person() {}

           public Person(String name, Integer age) {
               this.name = name;
               this.age = age;
           }

           public String toString() {
               return this.name.toString() + ": age " + this.age.toString();
           }
       }
   }
  ```

Przykładowa kompilacja i uruchomienie programu Java z terminala:
```bash
javac Example.java
java Example
```

lub zrobić jar:
```
javac TemperatureBelowZero.java
jar cfe TemperatureBelowZero.jar TemperatureBelowZero *.class
java -jar TemperatureBelowZero.jar
```

uruchomienie z flink:
```
# będąc w katalogu z plikiem TemperatureBelowZero.java
javac -cp "/sciezka/do/flink/lib/*" TemperatureBelowZero.java
jar cf TemperatureBelowZero.jar TemperatureBelowZero.class TemperatureBelowZero\$Temperature.class

# uruchomienie joba w Flink
/sciezka/do/flink/bin/flink run -c TemperatureBelowZero TemperatureBelowZero.jar
```


6. Napisz własny program w systemie Flink wykrywania temperatury poniżej zera.
  Dane dotyczące temperatury należy wygenerować.
7. W środowisku Flink uruchom opracowany program.
8. Napisz krótkie sprawozdanie (1-2 strony).

