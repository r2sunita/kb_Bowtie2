
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
 * Provide either a genome_ref or assembly_ref to get a Bowtie2 index for.
 * output_dir is optional, if provided the index files will be saved in that
 * directory.  If not, a directory will be generated for you and returned
 * by this function.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "genome_ref",
    "assembly_ref",
    "output_dir"
})
public class GetBowtie2Index {

    @JsonProperty("genome_ref")
    private String genomeRef;
    @JsonProperty("assembly_ref")
    private String assemblyRef;
    @JsonProperty("output_dir")
    private String outputDir;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("genome_ref")
    public String getGenomeRef() {
        return genomeRef;
    }

    @JsonProperty("genome_ref")
    public void setGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
    }

    public GetBowtie2Index withGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
        return this;
    }

    @JsonProperty("assembly_ref")
    public String getAssemblyRef() {
        return assemblyRef;
    }

    @JsonProperty("assembly_ref")
    public void setAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
    }

    public GetBowtie2Index withAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
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
        return ((((((((("GetBowtie2Index"+" [genomeRef=")+ genomeRef)+", assemblyRef=")+ assemblyRef)+", outputDir=")+ outputDir)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
