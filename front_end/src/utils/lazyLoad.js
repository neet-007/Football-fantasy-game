import {lazy} from "react";

export const lazyLoad = (path, namedExport=null) => {
    return lazy( async() => {
        const promise = import(path)
        if (namedExport === null){
            return promise
        }
        return promise.then(module => ({default: module[namedExport]}))
    })
}