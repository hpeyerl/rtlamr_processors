Contains some quick and dirty scripts to post-process the output of [rtlamr](https://github.com/bemasher/rtlamr) when used with the `-format json` argument.

* rtlamr_proc.py
    * accept records and put them in a mysql database. Schemas look like this:
    * `create table meters (t timestamp default current_timestamp, id varchar(20),type int, tamperphy int, tamperenc int, consumption int);`
    * `create table types (type int, commodity varchar(10);`
    
      I have pre-populated the 'types' table to look like this:
    
      * 5 - Electric
      * 11 - Water
      * 12 - Gas

   * A sample query looks like this:
     * `select meters.t,meters.consumption,types.commodity from meters inner join types on types.type=meters.type where types.commodity='Water' order by t desc;`

     
 * rtlamr_mqtt.py
     * accept records and publish them via MQTT.
     * Topic is `<meter ID>/vol`
     * This is used by me to get meter readings into [homeassistant](https://home-assistant.io/).  Here is my configuration.yaml:

```
- platform: mqtt
  state_topic: 39818788/vol
  name: "dr-gas-meter"
```

