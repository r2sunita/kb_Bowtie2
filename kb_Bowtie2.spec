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

    funcdef align_reads_to_assembly(AlignReadsParams params)
        returns () authentication required;


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
