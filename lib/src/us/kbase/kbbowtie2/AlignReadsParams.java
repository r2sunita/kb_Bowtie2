
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
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "reads_ref",
    "assembly_ref",
    "genome_ref",
    "output_name",
    "ws_id",
    "sampleset_id",
    "genome_id",
    "bowtie_index",
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

    @JsonProperty("reads_ref")
    private String readsRef;
    @JsonProperty("assembly_ref")
    private String assemblyRef;
    @JsonProperty("genome_ref")
    private String genomeRef;
    @JsonProperty("output_name")
    private String outputName;
    @JsonProperty("ws_id")
    private String wsId;
    @JsonProperty("sampleset_id")
    private String samplesetId;
    @JsonProperty("genome_id")
    private String genomeId;
    @JsonProperty("bowtie_index")
    private String bowtieIndex;
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

    @JsonProperty("reads_ref")
    public String getReadsRef() {
        return readsRef;
    }

    @JsonProperty("reads_ref")
    public void setReadsRef(String readsRef) {
        this.readsRef = readsRef;
    }

    public AlignReadsParams withReadsRef(String readsRef) {
        this.readsRef = readsRef;
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

    public AlignReadsParams withAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
        return this;
    }

    @JsonProperty("genome_ref")
    public String getGenomeRef() {
        return genomeRef;
    }

    @JsonProperty("genome_ref")
    public void setGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
    }

    public AlignReadsParams withGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
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

    @JsonProperty("ws_id")
    public String getWsId() {
        return wsId;
    }

    @JsonProperty("ws_id")
    public void setWsId(String wsId) {
        this.wsId = wsId;
    }

    public AlignReadsParams withWsId(String wsId) {
        this.wsId = wsId;
        return this;
    }

    @JsonProperty("sampleset_id")
    public String getSamplesetId() {
        return samplesetId;
    }

    @JsonProperty("sampleset_id")
    public void setSamplesetId(String samplesetId) {
        this.samplesetId = samplesetId;
    }

    public AlignReadsParams withSamplesetId(String samplesetId) {
        this.samplesetId = samplesetId;
        return this;
    }

    @JsonProperty("genome_id")
    public String getGenomeId() {
        return genomeId;
    }

    @JsonProperty("genome_id")
    public void setGenomeId(String genomeId) {
        this.genomeId = genomeId;
    }

    public AlignReadsParams withGenomeId(String genomeId) {
        this.genomeId = genomeId;
        return this;
    }

    @JsonProperty("bowtie_index")
    public String getBowtieIndex() {
        return bowtieIndex;
    }

    @JsonProperty("bowtie_index")
    public void setBowtieIndex(String bowtieIndex) {
        this.bowtieIndex = bowtieIndex;
    }

    public AlignReadsParams withBowtieIndex(String bowtieIndex) {
        this.bowtieIndex = bowtieIndex;
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
        return ((((((((((((((((((((((((((((((((((((((((("AlignReadsParams"+" [readsRef=")+ readsRef)+", assemblyRef=")+ assemblyRef)+", genomeRef=")+ genomeRef)+", outputName=")+ outputName)+", wsId=")+ wsId)+", samplesetId=")+ samplesetId)+", genomeId=")+ genomeId)+", bowtieIndex=")+ bowtieIndex)+", phred33=")+ phred33)+", phred64=")+ phred64)+", local=")+ local)+", veryFast=")+ veryFast)+", fast=")+ fast)+", verySensitive=")+ verySensitive)+", sensitive=")+ sensitive)+", veryFastLocal=")+ veryFastLocal)+", verySensitiveLocal=")+ verySensitiveLocal)+", fastLocal=")+ fastLocal)+", fastSensitive=")+ fastSensitive)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
