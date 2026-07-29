import os
import tempfile
from chemstractor.commands.combine import create_plots
def test_sankey():
    temp_dir = tempfile.mkdtemp()
    
    mock_data = {
        "run_info": {
            "total_papers_inputted": 10
        },
        "papers_summary": [
            {"source_paper": f"Paper_{i}.pdf", "flory_count": 3} for i in range(10)
        ],
        "flory_entries": [
            # Error free entries
            {
                "polymer_name": "poly(methyl methacrylate)",
                "solvent_name": "chloroform-d",
                "c_value": -0.5,
                "v_value": 0.5,
                "failed_fields": "None"
            },
            {
                "polymer_name": "polystyrene",
                "solvent_name": "toluene-d8",
                "c_value": -0.6,
                "v_value": 0.55,
                "failed_fields": {
                    "solvent_name": False,
                    "c_value_missing": False,
                    "c_value_out_of_range": False,
                    "v_value_missing": False,
                    "v_value_out_of_range": False,
                    "polymer_name": False,
                    "temperature_missing": False,
                    "D_out_of_range": False
                }
            },
            # Entry with polymer identification failure
            {
                "polymer_name": "N/A",
                "solvent_name": "benzene-d6",
                "failed_fields": {
                    "polymer_name": True,
                    "solvent_name": False,
                    "c_value_missing": False,
                    "c_value_out_of_range": False,
                    "v_value_missing": False,
                    "v_value_out_of_range": False,
                    "temperature_missing": False,
                    "D_out_of_range": False
                }
            },
            # Entry with v_value out of range and temperature missing
            {
                "polymer_name": "polyethylene",
                "solvent_name": "tetrahydrofuran-d8",
                "failed_fields": {
                    "polymer_name": False,
                    "solvent_name": False,
                    "c_value_missing": False,
                    "c_value_out_of_range": False,
                    "v_value_missing": False,
                    "v_value_out_of_range": True,
                    "temperature_missing": True,
                    "D_out_of_range": False
                }
            }
        ],
        "mark_houwink_entries": [],
        "failures": []
    }
    
    generated_plots = create_plots(temp_dir, mock_data)
    print("Generated plot paths:")
    for p in generated_plots:
        print(" -", p, "Exists:", os.path.exists(p))
        
    sankey_html = os.path.join(temp_dir, "plots", "flory_sankey_diagram.html")
    assert os.path.exists(sankey_html), f"Expected {sankey_html} to exist!"
    print("\nSUCCESS: Plotly Sankey diagram generated successfully!")
if __name__ == "__main__":
    test_sankey()