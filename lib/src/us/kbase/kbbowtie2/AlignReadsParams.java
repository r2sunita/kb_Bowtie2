
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
 * <p>Original spec-file type: AlignReadsParams</p>
 * <pre>
 * Will align the input reads (or set of reads specified in a SampleSet) to the specified
 * assembly or assembly for the specified Genome (accepts Assembly, ContigSet, or Genome types)
 * and produces a ReadsAlignment object, or in the case of a SampleSet, a ReadsAlignmentSet
 * object.
 * required:
 *     input_ref - ref to either a SingleEnd/PairedEnd reads, or a SampleSet input
 *                 (eventually should support a ReadsSet as well)
 *     assembly_or_genome - ref to Assembly, ContigSet, or Genome
 *     output_name - name of the output ReadsAlignment or ReadsAlignmentSet
 *     output_workspace - name or id of the WS to save the results to
 * optional:
 *     ...
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "input_ref",
    "assembly_or_genome_ref",
    "output_name",
    "output_workspace",
    "phred33",
    "phred64",
    "local",
    "very-fast",
    "fast",
    "very-sensitive",
    "sensitive",
    "very-fast-local",
    "very-sensitive-local",
    "fast-local",
    "fast-sensitive"
})
public class AlignReadsParams {

    @JsonProperty("input_ref")
    private String inputRef;
    @JsonProperty("assembly_or_genome_ref")
    private String assemblyOrGenomeRef;
    @JsonProperty("output_name")
    private String outputName;
    @JsonProperty("output_workspace")
    private String outputWorkspace;
    @JsonProperty("phred33")
    private String phred33;
    @JsonProperty("phred64")
    private String phred64;
    @JsonProperty("local")
    private String local;
    @JsonProperty("very-fast")
    private String veryFast;
    @JsonProperty("fast")
    private String fast;
    @JsonProperty("very-sensitive")
    private String verySensitive;
    @JsonProperty("sensitive")
    private String sensitive;
    @JsonProperty("very-fast-local")
    private String veryFastLocal;
    @JsonProperty("very-sensitive-local")
    private String verySensitiveLocal;
    @JsonProperty("fast-local")
    private String fastLocal;
    @JsonProperty("fast-sensitive")
    private String fastSensitive;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("input_ref")
    public String getInputRef() {
        return inputRef;
    }

    @JsonProperty("input_ref")
    public void setInputRef(String inputRef) {
        this.inputRef = inputRef;
    }

    public AlignReadsParams withInputRef(String inputRef) {
        this.inputRef = inputRef;
        return this;
    }

    @JsonProperty("assembly_or_genome_ref")
    public String getAssemblyOrGenomeRef() {
        return assemblyOrGenomeRef;
    }

    @JsonProperty("assembly_or_genome_ref")
    public void setAssemblyOrGenomeRef(String assemblyOrGenomeRef) {
        this.assemblyOrGenomeRef = assemblyOrGenomeRef;
    }

    public AlignReadsParams withAssemblyOrGenomeRef(String assemblyOrGenomeRef) {
        this.assemblyOrGenomeRef = assemblyOrGenomeRef;
        return this;
    }

    @JsonProperty("output_name")
    public String getOutputName() {
        return outputName;
    }

    @JsonProperty("output_name")
    public void setOutputName(String outputName) {
        this.outputName = outputName;
    }

    public AlignReadsParams withOutputName(String outputName) {
        this.outputName = outputName;
        return this;
    }

    @JsonProperty("output_workspace")
    public String getOutputWorkspace() {
        return outputWorkspace;
    }

    @JsonProperty("output_workspace")
    public void setOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
    }

    public AlignReadsParams withOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
        return this;
    }

    @JsonProperty("phred33")
    public String getPhred33() {
        return phred33;
    }

    @JsonProperty("phred33")
    public void setPhred33(String phred33) {
        this.phred33 = phred33;
    }

    public AlignReadsParams withPhred33(String phred33) {
        this.phred33 = phred33;
        return this;
    }

    @JsonProperty("phred64")
    public String getPhred64() {
        return phred64;
    }

    @JsonProperty("phred64")
    public void setPhred64(String phred64) {
        this.phred64 = phred64;
    }

    public AlignReadsParams withPhred64(String phred64) {
        this.phred64 = phred64;
        return this;
    }

    @JsonProperty("local")
    public String getLocal() {
        return local;
    }

    @JsonProperty("local")
    public void setLocal(String local) {
        this.local = local;
    }

    public AlignReadsParams withLocal(String local) {
        this.local = local;
        return this;
    }

    @JsonProperty("very-fast")
    public String getVeryFast() {
        return veryFast;
    }

    @JsonProperty("very-fast")
    public void setVeryFast(String veryFast) {
        this.veryFast = veryFast;
    }

    public AlignReadsParams withVeryFast(String veryFast) {
        this.veryFast = veryFast;
        return this;
    }

    @JsonProperty("fast")
    public String getFast() {
        return fast;
    }

    @JsonProperty("fast")
    public void setFast(String fast) {
        this.fast = fast;
    }

    public AlignReadsParams withFast(String fast) {
        this.fast = fast;
        return this;
    }

    @JsonProperty("very-sensitive")
    public String getVerySensitive() {
        return verySensitive;
    }

    @JsonProperty("very-sensitive")
    public void setVerySensitive(String verySensitive) {
        this.verySensitive = verySensitive;
    }

    public AlignReadsParams withVerySensitive(String verySensitive) {
        this.verySensitive = verySensitive;
        return this;
    }

    @JsonProperty("sensitive")
    public String getSensitive() {
        return sensitive;
    }

    @JsonProperty("sensitive")
    public void setSensitive(String sensitive) {
        this.sensitive = sensitive;
    }

    public AlignReadsParams withSensitive(String sensitive) {
        this.sensitive = sensitive;
        return this;
    }

    @JsonProperty("very-fast-local")
    public String getVeryFastLocal() {
        return veryFastLocal;
    }

    @JsonProperty("very-fast-local")
    public void setVeryFastLocal(String veryFastLocal) {
        this.veryFastLocal = veryFastLocal;
    }

    public AlignReadsParams withVeryFastLocal(String veryFastLocal) {
        this.veryFastLocal = veryFastLocal;
        return this;
    }

    @JsonProperty("very-sensitive-local")
    public String getVerySensitiveLocal() {
        return verySensitiveLocal;
    }

    @JsonProperty("very-sensitive-local")
    public void setVerySensitiveLocal(String verySensitiveLocal) {
        this.verySensitiveLocal = verySensitiveLocal;
    }

    public AlignReadsParams withVerySensitiveLocal(String verySensitiveLocal) {
        this.verySensitiveLocal = verySensitiveLocal;
        return this;
    }

    @JsonProperty("fast-local")
    public String getFastLocal() {
        return fastLocal;
    }

    @JsonProperty("fast-local")
    public void setFastLocal(String fastLocal) {
        this.fastLocal = fastLocal;
    }

    public AlignReadsParams withFastLocal(String fastLocal) {
        this.fastLocal = fastLocal;
        return this;
    }

    @JsonProperty("fast-sensitive")
    public String getFastSensitive() {
        return fastSensitive;
    }

    @JsonProperty("fast-sensitive")
    public void setFastSensitive(String fastSensitive) {
        this.fastSensitive = fastSensitive;
    }

    public AlignReadsParams withFastSensitive(String fastSensitive) {
        this.fastSensitive = fastSensitive;
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
        return ((((((((((((((((((((((((((((((((("AlignReadsParams"+" [inputRef=")+ inputRef)+", assemblyOrGenomeRef=")+ assemblyOrGenomeRef)+", outputName=")+ outputName)+", outputWorkspace=")+ outputWorkspace)+", phred33=")+ phred33)+", phred64=")+ phred64)+", local=")+ local)+", veryFast=")+ veryFast)+", fast=")+ fast)+", verySensitive=")+ verySensitive)+", sensitive=")+ sensitive)+", veryFastLocal=")+ veryFastLocal)+", verySensitiveLocal=")+ verySensitiveLocal)+", fastLocal=")+ fastLocal)+", fastSensitive=")+ fastSensitive)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
