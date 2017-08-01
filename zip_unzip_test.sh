for i in `seq 1 1000000`;
        do
                zip tux_out.zip tux_out.png
                rm tux_out.png
                unzip tux_out.zip 
        done   