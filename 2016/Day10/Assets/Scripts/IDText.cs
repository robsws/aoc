using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IDText : MonoBehaviour {

	// Use this for initialization
	void Start () {
        // Set the sort order for the text correctly
        MeshRenderer IdTextMesh = transform.GetComponent<MeshRenderer>();
        IdTextMesh.sortingLayerName = "Bot";
        IdTextMesh.sortingOrder = 3;
    }
	
	// Update is called once per frame
	void Update () {
		
	}

    public void SetID (int id) {
        TextMesh text = transform.GetComponent<TextMesh>();
        text.text = id.ToString();
    }
}
