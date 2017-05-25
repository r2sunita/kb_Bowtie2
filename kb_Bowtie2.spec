/*
A KBase module: kb_Bowtie2
*/

module kb_Bowtie2 {
    

    /*
    */
    typedef structure {

        string reads_ref;

        string assembly_ref;
        string genome_ref;

        string output_name;


        string ws_id;
        string sampleset_id;
        string genome_id;
        string bowtie_index;
        string phred33;
        string phred64;
        string local;
        string very-fast;
        string fast;
        string very-sensitive;
        string sensitive;
        string very-fast-local;
        string very-sensitive-local;
        string fast-local;
        string fast-sensitive;
    } AlignReadsParams;


    typedef structure {
        string reads_alignment_ref;

        string report_name;
        string report_ref;
    } AlignReadsResult;


    funcdef align_reads_to_assembly_app(AlignReadsParams params)
        returns (AlignReadsResult) authentication required;



    /* Provide either a genome_ref or assembly_ref to get a Bowtie2 index for.
       output_dir is optional, if provided the index files will be saved in that
       directory.  If not, a directory will be generated for you and returned
       by this function.
    */
    typedef structure {
        string genome_ref;
        string assembly_ref;
        string output_dir;
    } GetBowtie2Index;

    typedef structure {
        string output_dir;
    } GetBowtie2IndexResult;

    funcdef get_bowtie2_index(GetBowtie2Index params)
        returns(GetBowtie2IndexResult result) authentication required;

    /*
        supported commands:
            bowtie2
            bowtie2-align-l
            bowtie2-align-s

            bowtie2-build
            bowtie2-build-l
            bowtie2-build-s

            bowtie2-inspect
            bowtie2-inspect-l
            bowtie2-inspect-s
    */
    typedef structure {
        string command_name;
        list <string> options;
    } RunBowtie2CLIParams;

    /* general purpose local function for running tools in the bowtie2 suite */
    funcdef run_bowtie2_cli(RunBowtie2CLIParams params)
        returns () authentication required;
};
