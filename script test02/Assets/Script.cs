using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Script : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Transfprm Test");
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(Vector3.forward * Time.deltaTime);
        Debug.Log("Vector3.forward");
        Debug.Log(Vector3.forward);
    }
}
