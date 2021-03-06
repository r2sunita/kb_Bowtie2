/*
A KBase module: kb_Bowtie2
*/

module kb_Bowtie2 {
    
    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    /*
        Will align the input reads (or set of reads specified in a SampleSet) to the specified
        assembly or assembly for the specified Genome (accepts Assembly, ContigSet, or Genome types)
        and produces a ReadsAlignment object, or in the case of a SampleSet, a ReadsAlignmentSet
        object.

        required:
            input_ref - ref to either a SingleEnd/PairedEnd reads, or a SampleSet input
                        (eventually should support a ReadsSet as well)
            assembly_or_genome - ref to Assembly, ContigSet, or Genome
            output_name - name of the output ReadsAlignment or ReadsAlignmentSet
            output_workspace - name or id of the WS to save the results to

        optional:
            ...
    */
    typedef structure {

        string input_ref;

        string assembly_or_genome_ref;

        string output_name;
        string output_workspace;

        string output_obj_name_suffix;
        string output_alignment_suffix;

        string condition_label;

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

        string quality_score;
        string alignment_type;
        int trim5;
        int trim3;
        int np;
        string preset_options;
        int minins;
        int maxins;
        string orientation; 

        int concurrent_njsw_tasks;
        int concurrent_local_tasks;
    } AlignReadsParams;


    typedef structure {
        string reads_alignment_ref;
        string read_alignment_set_ref;

        string report_name;
        string report_ref;
    } AlignReadsResult;


    funcdef align_reads_to_assembly_app(AlignReadsParams params)
        returns (AlignReadsResult result) authentication required;


    /* aligns a single reads object to produce */
    funcdef align_one_reads_to_assembly()
        returns () authentication required;



    /* Provide a reference to either an Assembly or Genome to get a Bowtie2 index.

       output_dir is optional, if provided the index files will be saved in that
       directory.  If not, a directory will be generated for you and returned
       by this function.  If specifying the output_dir, the directory must not
       exist yet (to ensure only the index files are added there).
        
       Currently, Bowtie2 indexes are cached to a WS object.  If that object does
       not exist, then calling this function can create a new object.  To create
       the cache, you must specify the ws name or ID in 'ws_for_cache' in which
       to create the cached index.  If this field is not set, the result will
       not be cached.  This parameter will eventually be deprecated once the
       big file cache service is implemented.
    */
    typedef structure {
        string ref;
        string output_dir;
        string ws_for_cache;
    } GetBowtie2Index;

    /*
        output_dir - the folder containing the index files
        from_cache - 0 if the index was built fresh, 1 if it was found in the cache
        pushed_to_cache - if the index was rebuilt and successfully added to the
                          cache, this will be set to 1; otherwise set to 0
    */
    typedef structure {
        string output_dir;
        boolean from_cache;
        boolean pushed_to_cache;
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
