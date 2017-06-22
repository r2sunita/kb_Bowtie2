
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
 * <p>Original spec-file type: AlignReadsResult</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "reads_alignment_ref",
    "read_alignment_set_ref",
    "report_name",
    "report_ref"
})
public class AlignReadsResult {

    @JsonProperty("reads_alignment_ref")
    private String readsAlignmentRef;
    @JsonProperty("read_alignment_set_ref")
    private String readAlignmentSetRef;
    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_ref")
    private String reportRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("reads_alignment_ref")
    public String getReadsAlignmentRef() {
        return readsAlignmentRef;
    }

    @JsonProperty("reads_alignment_ref")
    public void setReadsAlignmentRef(String readsAlignmentRef) {
        this.readsAlignmentRef = readsAlignmentRef;
    }

    public AlignReadsResult withReadsAlignmentRef(String readsAlignmentRef) {
        this.readsAlignmentRef = readsAlignmentRef;
        return this;
    }

    @JsonProperty("read_alignment_set_ref")
    public String getReadAlignmentSetRef() {
        return readAlignmentSetRef;
    }

    @JsonProperty("read_alignment_set_ref")
    public void setReadAlignmentSetRef(String readAlignmentSetRef) {
        this.readAlignmentSetRef = readAlignmentSetRef;
    }

    public AlignReadsResult withReadAlignmentSetRef(String readAlignmentSetRef) {
        this.readAlignmentSetRef = readAlignmentSetRef;
        return this;
    }

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public AlignReadsResult withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public AlignReadsResult withReportRef(String reportRef) {
        this.reportRef = reportRef;
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
        return ((((((((((("AlignReadsResult"+" [readsAlignmentRef=")+ readsAlignmentRef)+", readAlignmentSetRef=")+ readAlignmentSetRef)+", reportName=")+ reportName)+", reportRef=")+ reportRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
