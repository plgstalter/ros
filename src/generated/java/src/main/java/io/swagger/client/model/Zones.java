/*
 * Strava API v3
 * The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.
 *
 * OpenAPI spec version: 3.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.client.model.HeartRateZoneRanges;
import io.swagger.client.model.PowerZoneRanges;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * Zones
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2021-10-24T21:35:10.561608+02:00[Europe/Rome]")
public class Zones {
  @SerializedName("heart_rate")
  private HeartRateZoneRanges heartRate = null;

  @SerializedName("power")
  private PowerZoneRanges power = null;

  public Zones heartRate(HeartRateZoneRanges heartRate) {
    this.heartRate = heartRate;
    return this;
  }

   /**
   * Get heartRate
   * @return heartRate
  **/
  @Schema(description = "")
  public HeartRateZoneRanges getHeartRate() {
    return heartRate;
  }

  public void setHeartRate(HeartRateZoneRanges heartRate) {
    this.heartRate = heartRate;
  }

  public Zones power(PowerZoneRanges power) {
    this.power = power;
    return this;
  }

   /**
   * Get power
   * @return power
  **/
  @Schema(description = "")
  public PowerZoneRanges getPower() {
    return power;
  }

  public void setPower(PowerZoneRanges power) {
    this.power = power;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Zones zones = (Zones) o;
    return Objects.equals(this.heartRate, zones.heartRate) &&
        Objects.equals(this.power, zones.power);
  }

  @Override
  public int hashCode() {
    return Objects.hash(heartRate, power);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Zones {\n");
    
    sb.append("    heartRate: ").append(toIndentedString(heartRate)).append("\n");
    sb.append("    power: ").append(toIndentedString(power)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
