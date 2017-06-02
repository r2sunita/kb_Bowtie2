
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
 * <p>Original spec-file type: GetBowtie2Index</p>
 * <pre>
 * Provide a reference to either an Assembly or Genome to get a Bowtie2 index.
 *        output_dir is optional, if provided the index files will be saved in that
 *        directory.  If not, a directory will be generated for you and returned
 *        by this function.  If specifying the output_dir, the directory must not
 *        exist yet (to ensure only the index files are added there).
 *         
 *        Currently, Bowtie2 indexes are cached to a WS object.  If that object does
 *        not exist, then calling this function can create a new object.  To create
 *        the cache, you must specify the ws name or ID in 'ws_for_cache' in which
 *        to create the cached index.  If this field is not set, the result will
 *        not be cached.  This parameter will eventually be deprecated once the
 *        big file cache service is implemented.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ref",
    "output_dir",
    "ws_for_cache"
})
public class GetBowtie2Index {

    @JsonProperty("ref")
    private String ref;
    @JsonProperty("output_dir")
    private String outputDir;
    @JsonProperty("ws_for_cache")
    private String wsForCache;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("ref")
    public String getRef() {
        return ref;
    }

    @JsonProperty("ref")
    public void setRef(String ref) {
        this.ref = ref;
    }

    public GetBowtie2Index withRef(String ref) {
        this.ref = ref;
        return this;
    }

    @JsonProperty("output_dir")
    public String getOutputDir() {
        return outputDir;
    }

    @JsonProperty("output_dir")
    public void setOutputDir(String outputDir) {
        this.outputDir = outputDir;
    }

    public GetBowtie2Index withOutputDir(String outputDir) {
        this.outputDir = outputDir;
        return this;
    }

    @JsonProperty("ws_for_cache")
    public String getWsForCache() {
        return wsForCache;
    }

    @JsonProperty("ws_for_cache")
    public void setWsForCache(String wsForCache) {
        this.wsForCache = wsForCache;
    }

    public GetBowtie2Index withWsForCache(String wsForCache) {
        this.wsForCache = wsForCache;
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
        return ((((((((("GetBowtie2Index"+" [ref=")+ ref)+", outputDir=")+ outputDir)+", wsForCache=")+ wsForCache)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
