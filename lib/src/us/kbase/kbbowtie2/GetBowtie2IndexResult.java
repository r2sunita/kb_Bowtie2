
package us.kbase.kbbowtie2;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: GetBowtie2IndexResult</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "output_dir"
})
public class GetBowtie2IndexResult {

    @JsonProperty("output_dir")
    private String outputDir;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("output_dir")
    public String getOutputDir() {
        return outputDir;
    }

    @JsonProperty("output_dir")
    public void setOutputDir(String outputDir) {
        this.outputDir = outputDir;
    }

    public GetBowtie2IndexResult withOutputDir(String outputDir) {
        this.outputDir = outputDir;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((("GetBowtie2IndexResult"+" [outputDir=")+ outputDir)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
