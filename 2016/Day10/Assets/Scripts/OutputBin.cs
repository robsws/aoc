using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OutputBin : MonoBehaviour {

    private List<GameObject> chips;

	// Use this for initialization
	void Start () {
        chips = new List<GameObject>();
	}

    public void GiveChip(GameObject chip) {
        chips.Add(chip);
        chip.transform.parent = transform;
        chip.transform.localPosition = new Vector3(0f, -0.5f, 0f);
    }
}
